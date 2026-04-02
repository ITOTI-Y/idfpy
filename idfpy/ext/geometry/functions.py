"""Pure geometry functions for 3-D polygons (Newell's method)."""

from __future__ import annotations

import math
from collections.abc import Sequence

Vertex3D = tuple[float, float, float]


def polygon_normal(vertices: Sequence[Vertex3D]) -> tuple[float, float, float]:
    """Compute the surface normal of a 3-D polygon using Newell's method.

    Returns the **unit** normal vector.  For a degenerate polygon (all
    collinear vertices) the zero vector ``(0, 0, 0)`` is returned.
    """
    n = len(vertices)
    if n < 3:
        return (0.0, 0.0, 0.0)

    nx = ny = nz = 0.0
    for i in range(n):
        curr = vertices[i]
        nxt = vertices[(i + 1) % n]
        nx += (curr[1] - nxt[1]) * (curr[2] + nxt[2])
        ny += (curr[2] - nxt[2]) * (curr[0] + nxt[0])
        nz += (curr[0] - nxt[0]) * (curr[1] + nxt[1])

    length = math.sqrt(nx * nx + ny * ny + nz * nz)
    if length == 0.0:
        return (0.0, 0.0, 0.0)
    return (nx / length, ny / length, nz / length)


def polygon_area_3d(vertices: Sequence[Vertex3D]) -> float:
    """Compute the area of a planar 3-D polygon using Newell's method.

    The polygon does **not** need to be convex.
    """
    n = len(vertices)
    if n < 3:
        return 0.0

    nx = ny = nz = 0.0
    for i in range(n):
        curr = vertices[i]
        nxt = vertices[(i + 1) % n]
        nx += (curr[1] - nxt[1]) * (curr[2] + nxt[2])
        ny += (curr[2] - nxt[2]) * (curr[0] + nxt[0])
        nz += (curr[0] - nxt[0]) * (curr[1] + nxt[1])

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
