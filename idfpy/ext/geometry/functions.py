"""Pure geometry functions for 3-D polygons (Newell's method)."""

from __future__ import annotations

import math
from collections.abc import Sequence

Vertex3D = tuple[float, float, float]


def _newell_vector(vertices: Sequence[Vertex3D]) -> tuple[float, float, float]:
    """Compute the raw (unnormalized) Newell cross-product vector."""
    nx = ny = nz = 0.0
    n = len(vertices)
    for i in range(n):
        curr = vertices[i]
        nxt = vertices[(i + 1) % n]
        nx += (curr[1] - nxt[1]) * (curr[2] + nxt[2])
        ny += (curr[2] - nxt[2]) * (curr[0] + nxt[0])
        nz += (curr[0] - nxt[0]) * (curr[1] + nxt[1])
    return nx, ny, nz


def polygon_normal(vertices: Sequence[Vertex3D]) -> tuple[float, float, float]:
    """Compute the surface normal of a 3-D polygon using Newell's method.

    Returns the **unit** normal vector.  For a degenerate polygon (all
    collinear vertices) the zero vector ``(0, 0, 0)`` is returned.
    """
    if len(vertices) < 3:
        return (0.0, 0.0, 0.0)

    nx, ny, nz = _newell_vector(vertices)
    length = math.sqrt(nx * nx + ny * ny + nz * nz)
    if length == 0.0:
        return (0.0, 0.0, 0.0)
    return (nx / length, ny / length, nz / length)


def polygon_area_3d(vertices: Sequence[Vertex3D]) -> float:
    """Compute the area of a planar 3-D polygon using Newell's method.

    The polygon does **not** need to be convex.
    """
    if len(vertices) < 3:
        return 0.0

    nx, ny, nz = _newell_vector(vertices)
    return 0.5 * math.sqrt(nx * nx + ny * ny + nz * nz)


def polygon_centroid(vertices: Sequence[Vertex3D]) -> tuple[float, float, float]:
    """Compute the centroid (arithmetic mean of vertices) of a 3-D polygon."""
    n = len(vertices)
    if n == 0:
        return (0.0, 0.0, 0.0)

    sx = sy = sz = 0.0
    for v in vertices:
        sx += v[0]
        sy += v[1]
        sz += v[2]
    return (sx / n, sy / n, sz / n)


def polygon_tilt(vertices: Sequence[Vertex3D]) -> float:
    """Compute the tilt angle (degrees) between outward normal and +Z axis.

    ``0°`` means the surface faces straight up (roof/ceiling exterior),
    ``90°`` is vertical (wall), and ``180°`` faces straight down (floor
    exterior).  Returns ``0.0`` for degenerate polygons.  Range ``[0, 180]``.
    """
    nx, ny, nz = polygon_normal(vertices)
    if nx == 0.0 and ny == 0.0 and nz == 0.0:
        return 0.0
    # Clamp to guard against floating point drift outside [-1, 1].
    nz_clamped = max(-1.0, min(1.0, nz))
    return math.degrees(math.acos(nz_clamped))


def polygon_azimuth(vertices: Sequence[Vertex3D]) -> float:
    """Compute the surface azimuth (degrees), clockwise from north (+Y).

    Follows the EnergyPlus convention: ``N=0, E=90, S=180, W=270``.  The
    angle is derived from the projection of the outward normal onto the
    XY plane.  Purely horizontal surfaces have an undefined azimuth and
    return ``0.0``.  Range ``[0, 360)``.
    """
    nx, ny, _ = polygon_normal(vertices)
    if math.sqrt(nx * nx + ny * ny) < 1e-9:
        return 0.0
    angle = math.degrees(math.atan2(nx, ny))
    return angle % 360.0


def polygon_perimeter(vertices: Sequence[Vertex3D]) -> float:
    """Compute the perimeter of a closed polygon as the sum of edge lengths.

    Returns ``0.0`` for degenerate inputs with fewer than 3 vertices.
    """
    n = len(vertices)
    if n < 3:
        return 0.0

    total = 0.0
    for i in range(n):
        curr = vertices[i]
        nxt = vertices[(i + 1) % n]
        dx = nxt[0] - curr[0]
        dy = nxt[1] - curr[1]
        dz = nxt[2] - curr[2]
        total += math.sqrt(dx * dx + dy * dy + dz * dz)
    return total


def polygon_bounding_box(
    vertices: Sequence[Vertex3D],
) -> tuple[Vertex3D, Vertex3D]:
    """Compute the axis-aligned bounding box of a 3-D polygon.

    Returns ``((xmin, ymin, zmin), (xmax, ymax, zmax))``.  For an empty
    vertex list both corners are the origin ``(0, 0, 0)``.
    """
    if not vertices:
        return ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0))

    x0, y0, z0 = vertices[0]
    xmin = xmax = x0
    ymin = ymax = y0
    zmin = zmax = z0
    for x, y, z in vertices[1:]:
        if x < xmin:
            xmin = x
        elif x > xmax:
            xmax = x
        if y < ymin:
            ymin = y
        elif y > ymax:
            ymax = y
        if z < zmin:
            zmin = z
        elif z > zmax:
            zmax = z
    return ((xmin, ymin, zmin), (xmax, ymax, zmax))


def polygon_is_convex(vertices: Sequence[Vertex3D]) -> bool:
    """Return ``True`` if the planar polygon is convex.

    Walks each vertex triple and projects the cross product of the
    incoming/outgoing edges onto the polygon normal.  Collinear triples
    (zero cross product) are tolerated — only a sign flip among non-zero
    projections indicates a reflex vertex.  Degenerate polygons
    (fewer than 3 vertices, or a zero normal) return ``False``.
    """
    n = len(vertices)
    if n < 3:
        return False

    nxv, nyv, nzv = polygon_normal(vertices)
    if nxv == 0.0 and nyv == 0.0 and nzv == 0.0:
        return False

    sign = 0
    for i in range(n):
        prev = vertices[i - 1]
        curr = vertices[i]
        nxt = vertices[(i + 1) % n]

        e1x = curr[0] - prev[0]
        e1y = curr[1] - prev[1]
        e1z = curr[2] - prev[2]
        e2x = nxt[0] - curr[0]
        e2y = nxt[1] - curr[1]
        e2z = nxt[2] - curr[2]

        cx = e1y * e2z - e1z * e2y
        cy = e1z * e2x - e1x * e2z
        cz = e1x * e2y - e1y * e2x

        dot = cx * nxv + cy * nyv + cz * nzv
        if abs(dot) < 1e-9:
            continue
        current_sign = 1 if dot > 0 else -1
        if sign == 0:
            sign = current_sign
        elif sign != current_sign:
            return False
    return True
