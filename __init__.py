# Copyright 2015 Bassam Kurdali / urchn.org
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
# topsort.py copyright 2014 Sunlight Labs/ written by Paul Tagliometti
# forked from tasker, initially a tube addon

bl_info = {
    "name": "OrgNodes",
    "author": "Bassam Kurdali,Port to 2.80 by Zebus3d & Sav Martin",
    "version": (0, 0),
    "blender": (2, 80, 0),
    "location": "Node Editor > Tools",
    "description": "Project Task Manager",
    "warning": "",
    "wiki_url": "",
    "category": "Nodes"}

if "bpy" in locals():
    import importlib
    importlib.reload(depnodes)
else:
    from . import depnodes

import bpy

def register():
    depnodes.register()

def unregister():
    depnodes.unregister()

if __name__ == "__main__":
    register()
