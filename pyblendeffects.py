#!/usr/bin/python
# -*- coding: utf-8 -*-

"""ESA 3 in Objektorientierte Skriptspachen
   Die Technologie mit der wir uns im Semesterabschlussprojekt beschäftigen wird Blender sein.
   Es soll eine Automatisierung von Blender mit Hilfe von Python erfolgen. Dadurch soll auch dem
   Laien ermöglich werden, Schrift-Effekte zu generieren, die dann als fertiges Video gerendet werden.
   Diese kurzen Videos können dann beispielsweise direkt auf eine Webseite eingebunden, oder
   als Vorspann vor ein eigentliches Video gelegt werden.

Usage:
  pyblendeffects.py effect (dissolve|glossy) <text>
"""

__author__ = 'reinschs@fh-brandenburg.de | patrick.walther.1989@gmx.de | mommert@fh-brandenburg.de'

import bpy
import sys
from HtmlRenderer import HtmlRenderer

# Funktion für den Dissolve-Effekt
def DissolveEffect(text):
    print('DissolveEffect')

    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.delete(use_global=False)
    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.window.screen.areas[1].spaces[0].context = 'MATERIAL'
    mat_name = "andre"
    bpy.data.materials.new(mat_name)
    bpy.data.materials[mat_name].use_nodes = True
    bpy.data.materials[mat_name].node_tree.nodes['Diffuse BSDF'].inputs['Color'].default_value = (0.8, 0.719635, 0, 1)
    in_1 = bpy.data.materials[mat_name].node_tree.nodes["Material Output"].inputs["Surface"]
    out_1 = bpy.data.materials[mat_name].node_tree.nodes["Diffuse BSDF"].outputs["BSDF"]
    bpy.data.materials[mat_name].node_tree.links.new(in_1, out_1)
    bpy.data.objects["Cube"].active_material = bpy.data.materials[mat_name]
    bpy.ops.object.move_to_layer(layers=(False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    #bpy.data.window_managers["WinMan"].(null)[1] = True
    bpy.ops.object.text_add(view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), release_confirm=False)
    bpy.ops.object.editmode_toggle()
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    for c in text:
        bpy.ops.font.text_insert(text=c, accent=False))
    bpy.ops.object.editmode_toggle()
    bpy.context.window.screen.areas[1].spaces[0].context = 'DATA'
    bpy.context.object.data.extrude = 0.05
    bpy.context.object.data.bevel_depth = 0.02
    bpy.context.object.data.bevel_resolution = 2
    bpy.context.window.screen.areas[1].spaces[0].context = 'MATERIAL'
    bpy.data.objects["Text"].active_material = bpy.data.materials[mat_name]
    bpy.ops.object.convert(target='MESH', keep_original=False)
    bpy.context.window.screen.areas[1].spaces[0].context = 'RENDER'
    bpy.context.scene.frame_end = 135
    bpy.context.window.screen.areas[1].spaces[0].context = 'PARTICLES'
    bpy.ops.object.particle_system_add()
    bpy.data.particles["ParticleSettings"].frame_start = 20
    bpy.data.particles["ParticleSettings"].frame_end = 30
    bpy.data.particles["ParticleSettings"].lifetime = 100
    bpy.data.particles["ParticleSettings"].distribution = 'RAND'
    bpy.data.particles["ParticleSettings"].render_type = 'OBJECT'
    bpy.data.particles["ParticleSettings"].dupli_object = bpy.data.objects["Cube"]
    bpy.data.particles["ParticleSettings"].particle_size = 0.01
    bpy.data.particles["ParticleSettings"].effector_weights.gravity = 0
    bpy.data.particles["ParticleSettings"].normal_factor = 0
    bpy.ops.object.effector_add(type='TURBULENCE', view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.transform.translate(value=(2.5, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
    bpy.context.window.screen.areas[1].spaces[0].context = 'PHYSICS'
    bpy.context.object.field.strength = 2
    bpy.context.window.screen.areas[1].spaces[0].context = 'PARTICLES'
    bpy.data.objects['Text'].particle_systems["ParticleSystem"].settings.keyframe_insert(data_path="use_render_emitter", frame=1.0)
    bpy.context.scene.frame_current = 30
    bpy.data.objects['Text'].particle_systems["ParticleSystem"].settings.keyframe_insert(data_path="use_render_emitter", frame=30.0)
    bpy.context.scene.frame_current = 31
    bpy.data.particles["ParticleSettings"].use_render_emitter = False
    bpy.data.objects['Text'].particle_systems["ParticleSystem"].settings.keyframe_insert(data_path="use_render_emitter", frame=31.0)
    bpy.context.scene.frame_current = 70
    bpy.data.objects['Text'].particle_systems["ParticleSystem"].settings.keyframe_insert(data_path="particle_size", frame=70.0)
    bpy.context.scene.frame_current = 130
    bpy.data.particles["ParticleSettings"].particle_size = 0.001
    bpy.ops.mesh.primitive_plane_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.transform.translate(value=(0, 0, -0.1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
    bpy.ops.transform.resize(value=(100, 100, 100), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
    bpy.context.window.screen.areas[1].spaces[0].context = 'MATERIAL'
    bpy.context.window.screen.areas[1].spaces[0].context = 'CONSTRAINT'
    bpy.context.window.screen.areas[1].spaces[0].context = 'PHYSICS'
    bpy.ops.object.modifier_add(type='COLLISION')
    bpy.ops.object.lamp_add(type='POINT', view_align=False, location=(0, 0, 0), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.transform.translate(value=(0, 0, 5), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
    bpy.ops.transform.translate(value=(0, -5, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
    bpy.ops.transform.translate(value=(-6, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
    bpy.context.window.screen.areas[1].spaces[0].context = 'DATA'
    bpy.context.object.data.shadow_soft_size = 3
    bpy.data.lamps['Point'].node_tree.nodes['Emission'].inputs['Strength'].default_value = 5000
    #bpy.data.node_groups["Shader Nodetree"].nodes["Emission"].inputs[1].default_value = 5000

    bpy.ops.object.camera_add(view_align=True, enter_editmode=False, location=(0, 0, 0), rotation=(1.26972, 0.0140788, -0.375695), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    #bpy.ops.view3d.camera_to_view()
    bpy.ops.transform.translate(value=(0.32114, -0.119701, 0.0160501), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
    bpy.ops.transform.translate(value=(0, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
    bpy.context.object.location[1] = -5.34897
    bpy.context.object.rotation_euler[1] = 0.0140848
    bpy.context.window.screen.areas[1].spaces[0].context = 'WORLD'
    bpy.context.scene.world.horizon_color = (0, 0, 0)
    bpy.context.scene.world.horizon_color = (0, 0, 0)
    bpy.context.window.screen.areas[1].spaces[0].context = 'PHYSICS'
    bpy.data.particles["ParticleSettings"].count = 20000
    bpy.context.window.screen.areas[1].spaces[0].context = 'RENDER'
    bpy.context.scene.cycles.samples = 50
    bpy.context.scene.render.filepath = "/tmp/"
    bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
    bpy.context.scene.frame_current = 1



# Funktion für den Glossy-Effekt
def GlossyEffect(text):
    print('Glossy')

    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.delete(use_global=False)
    bpy.ops.object.text_add(view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), release_confirm=False)
    bpy.ops.object.editmode_toggle()
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    for c in text:
        bpy.ops.font.text_insert(text=c, accent=False)
    bpy.ops.object.editmode_toggle()
    #bpy.context.space_data.context = 'DATA'
    bpy.context.window.screen.areas[1].spaces[0].context = 'DATA'
    bpy.context.object.data.extrude = 0.3
    bpy.context.object.data.extrude = 0.3
    bpy.context.object.data.bevel_depth = 0.03
    bpy.context.object.data.bevel_resolution = 3
    bpy.context.object.data.extrude = 0.2
    bpy.context.scene.render.engine = 'CYCLES'
    #bpy.context.space_data.context = 'MATERIAL'
    bpy.context.window.screen.areas[1].spaces[0].context = 'MATERIAL'
    matName = "objMaterial"
    bpy.data.materials.new(matName)
    bpy.data.materials[matName].use_nodes = True
    bpy.data.node_groups["Shader Nodetree"].nodes["Glossy BSDF"].inputs[0].default_value = (0.8, 0.419435, 0.0352662, 1)
    bpy.data.node_groups["Shader Nodetree"].nodes["Glossy BSDF"].inputs[0].default_value = (0.8, 0.419435, 0.0352662, 1)
    bpy.ops.object.camera_add(view_align=True, enter_editmode=False, location=(0, 0, 0), rotation=(1.10871, 0.0132652, 1.14827), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.view3d.camera_to_view()
    bpy.ops.object.lamp_add(type='POINT', view_align=False, location=(0, 0, 0), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.transform.translate(value=(0, -2, -2), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
    bpy.context.object.data.shadow_soft_size = 1
    bpy.data.node_groups["Shader Nodetree"].nodes["Emission"].inputs[1].default_value = 5000
    #bpy.context.space_data.context = 'WORLD'
    bpy.context.window.screen.areas[1].spaces[0].context = 'WORLD'
    bpy.context.scene.world.horizon_color = (0, 0, 0)
    bpy.context.scene.world.horizon_color = (0, 0, 0)
    bpy.ops.transform.translate(value=(1.7, 0, 1), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
    #bpy.context.space_data.context = 'DATA'
    bpy.context.window.screen.areas[1].spaces[0].context = 'DATA'
    #bpy.context.space_data.context = 'MATERIAL'
    bpy.context.window.screen.areas[1].spaces[0].context = 'MATERIAL'
    bpy.data.node_groups["Shader Nodetree"].nodes["Glossy BSDF"].inputs[1].default_value = 0.3
    bpy.ops.transform.translate(value=(0, 0, -1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
    #TODO SWITCH WINDOW
    bpy.context.scene.use_nodes = True
    bpy.ops.node.add_node(use_transform=True, type="CompositorNodeGlare", settings=[])
    bpy.ops.transform.translate(value=(-135.307, 343.551, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)



# Haupteinstiegspunk
if __name__ == "__main__":
    arguments = sys.argv
    text = arguments[5]

    # Welcher Effekt soll generiert werden
    if arguments[4] == "dissolve":
        DissolveEffect(text)
    elif arguments[4] == "glossy":
        GlossyEffect(text)

    html_renderer = HtmlRenderer()
    print(html_renderer.get_text())
