# Copyright 2015 Bassam Kurdali / urchn.org
# Modified from custom nodes template
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

""" Visualize Project Task in Blender """

if "bpy" in locals():
    import importlib
    importlib.reload(taskdna)
else:
    from . import taskdna

import bpy

# TODO everything design evaluation/research and execution
# use a treemap, possibly using this library:
# squarify https://github.com/laserson/squarify
# must add visualizations into tasks - color code based on types, possibly
# doable in taskdna


def register():
    pass


def unregister():
    pass
