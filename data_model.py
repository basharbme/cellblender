# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.#
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

# <pep8 compliant>

"""
This file contains the classes defining and handling the CellBlender Data Model.
The CellBlender Data Model is intended to be a fairly stable representation of
a CellBlender project which should be compatible across CellBlender versions.
"""


"""
  CONVERSION NOTES:
    How do our CellBlender reaction fields/controls handle catalytic reactions?
    Would it be better to allow a full reaction expression rather than reactants/products?
    Should we have an option for using full reaction syntax?
    What is the MCellReactionsPanelProperty.reaction_name_list? Is it needed any more?
    
    MCellMoleculeReleaseProperty:
       Do we still need location, or is it handled by location_x,y,z?

    Release Patterns:

      class MCELL_PT_molecule_release(bpy.types.Panel):

            layout.prop_search(rel, "pattern", mcell.release_patterns,
                               "release_pattern_rxn_name_list",
                               icon='FORCE_LENNARDJONES')

        changed to:

            layout.prop_search(rel, "pattern", mcell.release_patterns,
                               "release_pattern_list",
                               icon='FORCE_LENNARDJONES')

      Should "release pattern" be called "release timing" or "release train"?

      Why does MCellReleasePatternPanelProperty contain:
         release_pattern_rxn_name_list?
       
"""


# blender imports
import bpy
from bpy.props import BoolProperty, CollectionProperty, EnumProperty, \
                      FloatProperty, FloatVectorProperty, IntProperty, \
                      IntVectorProperty, PointerProperty, StringProperty
from bpy.app.handlers import persistent

# python imports
import pickle

from bpy_extras.io_utils import ExportHelper
import cellblender
# import cellblender/cellblender_id


def code_api_version():
    return 1


data_model_depth = 0
def dump_data_model ( name, dm ):
    global data_model_depth
    if type(dm) == type({'a':1}):  #dm is a dictionary
        print ( str(data_model_depth*"  ") + name + " {}" )
        data_model_depth += 1
        for k,v in sorted(dm.items()):
            dump_data_model ( k, v )
        data_model_depth += -1
    elif type(dm) == type(['a',1]):  #dm is a list
        print ( str(data_model_depth*"  ") + name + " []" )
        data_model_depth += 1
        i = 0
        for v in dm:
            k = name + "["+str(i)+"]"
            dump_data_model ( k, v )
            i += 1
        data_model_depth += -1
    elif (type(dm) == type('a1')) or (type(dm) == type(u'a1')):  #dm is a string
        print ( str(data_model_depth*"  ") + name + " = " + "\"" + str(dm) + "\"" )
    else:
        print ( str(data_model_depth*"  ") + name + " = " + str(dm) )


def pickle_data_model ( dm ):
    return ( pickle.dumps(dm,protocol=0).decode('latin1') )

def unpickle_data_model ( dmp ):
    return ( pickle.loads ( dmp.encode('latin1') ) )


class PrintDataModel(bpy.types.Operator):
    '''Print the CellBlender data model to the console'''
    bl_idname = "cb.print_data_model" 
    bl_label = "Print Data Model"
    bl_description = "Print the CellBlender Data Model to the console"

    def execute(self, context):
        print ( "Printing CellBlender Data Model:" )
        mcell_dm = context.scene.mcell.build_data_model_from_properties ( context )
        dump_data_model ( "Data Model", {"mcell": mcell_dm} )
        return {'FINISHED'}


class ExportDataModel(bpy.types.Operator, ExportHelper):
    '''Export the CellBlender model as a Python Pickle in a text file'''
    bl_idname = "cb.export_data_model" 
    bl_label = "Export Data Model"
    bl_description = "Export CellBlender Data Model to a Python Pickle in a file"

    filename_ext = ".txt"
    filter_glob = StringProperty(default="*.txt",options={'HIDDEN'},)

    def execute(self, context):
        print ( "Saving CellBlender model to file: " + self.filepath )
        mcell_dm = context.scene.mcell.build_data_model_from_properties ( context )
        dm = { 'mcell': mcell_dm }
        f = open ( self.filepath, 'w' )
        f.write ( pickle_data_model(dm) )
        f.close()
        print ( "Done saving CellBlender model." )
        return {'FINISHED'}


class ExportDataModelAll(bpy.types.Operator, ExportHelper):
    '''Export the CellBlender model including geometry as a Python Pickle in a text file'''
    bl_idname = "cb.export_data_model_all" 
    bl_label = "Export Data Model with Geometry"
    bl_description = "Export CellBlender Data Model and Geometry to a Python Pickle in a file"

    filename_ext = ".txt"
    filter_glob = StringProperty(default="*.txt",options={'HIDDEN'},)

    def execute(self, context):
        print ( "Saving CellBlender model and geometry to file: " + self.filepath )
        mcell_dm = context.scene.mcell.build_data_model_from_properties ( context, geometry=True )
        dm = { 'mcell': mcell_dm }
        f = open ( self.filepath, 'w' )
        f.write ( pickle_data_model(dm) )
        f.close()
        print ( "Done saving CellBlender model." )
        return {'FINISHED'}


class ImportDataModel(bpy.types.Operator, ExportHelper):
    '''Import a CellBlender model from a Python Pickle in a text file'''
    bl_idname = "cb.import_data_model" 
    bl_label = "Import Data Model"
    bl_description = "Import CellBlender Data Model from a Python Pickle in a file"

    filename_ext = ".txt"
    filter_glob = StringProperty(default="*.txt",options={'HIDDEN'},)

    def execute(self, context):
        print ( "Loading CellBlender model from file: " + self.filepath + " ..." )
        f = open ( self.filepath, 'r' )
        pickle_string = f.read()
        f.close()

        dm = unpickle_data_model ( pickle_string )
        context.scene.mcell.build_properties_from_data_model ( context, dm['mcell'] )

        print ( "Done loading CellBlender model." )
        return {'FINISHED'}


class ImportDataModelAll(bpy.types.Operator, ExportHelper):
    '''Import a CellBlender model from a Python Pickle in a text file'''
    bl_idname = "cb.import_data_model_all" 
    bl_label = "Import Data Model with Geometry"
    bl_description = "Import CellBlender Data Model and Geometry from a Python Pickle in a file"

    filename_ext = ".txt"
    filter_glob = StringProperty(default="*.txt",options={'HIDDEN'},)

    def execute(self, context):
        print ( "Loading CellBlender model from file: " + self.filepath + " ..." )
        f = open ( self.filepath, 'r' )
        pickle_string = f.read()
        f.close()

        dm = unpickle_data_model ( pickle_string )
        context.scene.mcell.build_properties_from_data_model ( context, dm['mcell'], geometry=True )

        print ( "Done loading CellBlender model." )
        return {'FINISHED'}



# Construct the data model property
@persistent
def save_pre(context):
    """Set the "saved_by_source_id" value and store a data model based on the current property settings in this application"""
    # The context appears to always be "None"
    print ( "========================================" )
    source_id = cellblender.cellblender_info['cellblender_source_sha1']
    print ( "save_pre() has been called ... source_id = " + source_id )
    if not context:
        # The context appears to always be "None", so use bpy.context
        context = bpy.context
    if hasattr ( context.scene, 'mcell' ):
        print ( "Updating source ID of mcell before saving" )
        mcell = context.scene.mcell
        mcell['saved_by_source_id'] = source_id
        dm = mcell.build_data_model_from_properties ( context )
        context.scene.mcell['data_model'] = pickle_data_model(dm)
    print ( "========================================" )


    """
    print ( "data_model.save_pre called" )

    if not context:
        context = bpy.context

    if 'mcell' in context.scene:
        dm = context.scene.mcell.build_data_model_from_properties ( context )
        context.scene.mcell['data_model'] = pickle_data_model(dm)

    return
    """


# Check for a data model in the properties
@persistent
def load_post(context):
    """Detect whether the loaded .blend file matches the current addon and set a flag to be used by other code"""

    print ( "load post handler: data_model.load_post() called" )

    source_id = cellblender.cellblender_info['cellblender_source_sha1']
    print ( "cellblender source id = " + source_id )

    if not context:
        # The context appears to always be "None", so use bpy.context
        context = bpy.context

    api_version_in_blend_file = -1  # TODO May not be used

    #if 'mcell' in context.scene:
    if hasattr ( context.scene, 'mcell' ):
        mcell = context.scene.mcell

        mcell.versions_match = False
        if 'saved_by_source_id' in mcell:
            saved_by_id = mcell['saved_by_source_id']
            print ( "load_post() opened a blend file with source_id = " + saved_by_id )
            if source_id == saved_by_id:
                mcell.versions_match = True
            else:
                # Don't update the properties here. Just flag to display the "Upgrade" button for user to choose.
                mcell.versions_match = False
    print ( "End of load_post(): mcell.versions_match = " + str(mcell.versions_match) )
    print ( "========================================" )

    """
    # OLD Code before December 23rd, 2014:
    
        if 'api_version' in mcell:
            api_version_in_blend_file = mcell['api_version']

        print ( "Code API = " + str(code_api_version()) + ", File API = " + str(api_version_in_blend_file) )

        if (api_version_in_blend_file <= 0):

            # There is no data model (or it's experimental) so build one from the properties
            print ( "Building a data model from existing properties..." )
            dm = context.scene.mcell.build_data_model_from_properties ( context )
            context.scene.mcell['data_model'] = pickle_data_model(dm)

        elif (api_version_in_blend_file != code_api_version()):

            # There is a data model in the file so convert it to match current properties
            print ( "Building properties from the data model in the .blend file..." )
            dm = unpickle_data_model ( context.scene.mcell['data_model'] )
            context.scene.mcell.build_properties_from_data_model ( context, dm )
            context.scene['mcell']['api_version'] = code_api_version()

        else:

            # There is a data model in the file and it matches this version so just report it:
            print ( "API version in .blend file matches code ... no action needed." )

        # Uncomment this when we're ready to start producing public .blend files with API>0
        # context.scene['mcell']['api_version'] = code_api_version()

    else:
        print ( "context.scene does not have an 'mcell' key ... no data model to import" )

    return
    """


def menu_func_import(self, context):
    self.layout.operator("cb.import_data_model", text="Import CellBlender Model (text/pickle)")

def menu_func_export(self, context):
    self.layout.operator("cb.export_data_model", text="Export CellBlender Model (text/pickle)")

def menu_func_import_all(self, context):
    self.layout.operator("cb.import_data_model_all", text="Import CellBlender Model and Geometry (text/pickle)")

def menu_func_export_all(self, context):
    self.layout.operator("cb.export_data_model_all", text="Export CellBlender Model and Geometry (text/pickle)")

def menu_func_print(self, context):
    self.layout.operator("cb.print_data_model", text="Print CellBlender Model (text)")


# We use per module class registration/unregistration
def register():
    bpy.utils.register_module(__name__)
    #bpy.types.INFO_MT_file_export.append(menu_func_export_dm)

def unregister():
    bpy.utils.unregister_module(__name__)
    #bpy.types.INFO_MT_file_import.remove(menu_func_export_dm)


if __name__ == "__main__": 
    register()
