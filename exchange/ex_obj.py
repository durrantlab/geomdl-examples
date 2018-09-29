#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018

    Exporting a NURBS surface as .obj file
"""

from geomdl.shapes import surface
from geomdl import exchange

cylinder = surface.cylinder(radius=5.0, height=22.5)

# Export the surface as a .obj file
exchange.export_obj(cylinder, "cylindrical_surface.obj")

# Good to have something here to put a breakpoint
pass
