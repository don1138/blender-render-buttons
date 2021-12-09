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

# Shamelessly adapted from "Blender 2.80 Render Buttons", created by Mitsuma and modified by Olaf Haag
# Updated to be compatable with Blende 3.0

bl_info = {
	"name"       : "Render Buttons",
	"author"     : "Don Schnitzius",
	"version"    : (1, 0, 0),
	"blender"    : (3, 0, 0),
	"location"   : "Properties > Render Properties > Render",
	"description": "Quick Access to Render Controls",
	"warning"    : "",
	"wiki_url"   : "",
	"tracker_url": "",
	"category"   : "Render"}

import bpy

class AddRenderButtons(bpy.types.Panel):
	"""Creates a Panel in the render properties window"""
	bl_label       = "Render"
	bl_idname      = "OBJECT_PT_Add_Render"
	bl_space_type  = 'PROPERTIES'
	bl_region_type = 'WINDOW'
	bl_context     = "render"

	def draw(self, context):
		layout = self.layout

		pv = context.preferences.view
		rd = context.scene.render

		row = layout.row(align=True)
		row.operator("render.render", text="Render", icon='RENDER_STILL')
		row.operator("render.render", text="Animation", icon='RENDER_ANIMATION').animation = True

		split = layout.split()

		split.label(text="Display:")
		row = split.row(align=True)
		row.prop(pv, "render_display_type", text="")
		row.prop(rd, "use_lock_interface", icon_only=True)

def register():
	bpy.utils.register_class(AddRenderButtons)

def unregister():
	bpy.utils.unregister_class(AddRenderButtons)

if __name__ == "__main__":
	register()
