import os
import subprocess
import sys
import pickle
import shutil

import cellblender
from . import data_model_to_mdl_3r
from . import run_data_model_mcell_3r

print ( "Executing MCellR Simulation" )

# Name of this engine to display in the list of choices (Both should be unique within a CellBlender installation)
plug_code = "MCELLR"
plug_name = "MCell Rules"

def print_info():
  global parameter_dictionary
  print ( 50*'==' )
  for k in sorted(parameter_dictionary.keys()):
    print ( "" + k + " = " + str(parameter_dictionary[k]) )
  print ( 50*'==' )

def reset():
  global parameter_dictionary
  print ( "Reset was called" )
  parameter_dictionary['Output Detail (0-100)']['val'] = 20

# Get data from Blender / CellBlender
import bpy
mcell_path = ""
bionetgen_path = ""
nfsim_path = ""
try:
  mcell_path = bpy.context.scene.mcell.cellblender_preferences.mcell_binary
except:
  mcell_path = ""


# List of parameters as dictionaries - each with keys for 'name', 'desc', 'def', and optional 'as':
parameter_dictionary = {
  'MCellR Path':    {'val': mcell_path,     'as':'filename', 'desc':"MCellR Path",    'icon':'FORCE_LENNARDJONES'},
  'BioNetGen Path': {'val': bionetgen_path, 'as':'filename', 'desc':"BioNetGen Path", 'icon':'OUTLINER_DATA_MESH'},
  'NFSim Path':     {'val': nfsim_path,     'as':'filename', 'desc':"NFSim Path",     'icon':'DRIVER'},
  'Output Detail (0-100)': {'val': 20, 'desc':"Amount of Information to Print (0-100)", 'icon':'INFO'},
  'Print Information': {'val': print_info, 'desc':"Print information about Limited Python Simulation"},
  'Reset': {'val': reset, 'desc':"Reset everything"}
}

parameter_layout = [
  ['MCellR Path'],
  ['BioNetGen Path'],
  ['NFSim Path'],
  ['Output Detail (0-100)'],
  ['Print Information', 'Reset']
]


def prepare_runs ( data_model, project_dir, data_layout=None ):

  """ Arguments to:  run_mcell_sweep ( sys_argv, data_model=None )
    arg_parser = argparse.ArgumentParser(description='Run MCell with appropriate arguments')
    arg_parser.add_argument ( '-dm', '--data_model_file_name',     type=str, default='',        help='the file name of the data model to run' )
    arg_parser.add_argument ( '-pd', '--proj_dir',        type=str, default='',        help='the directory where the program will run' )
    arg_parser.add_argument ( '-b',  '--binary',          type=str, default='mcell',   help='full path of binary file to run' )
    arg_parser.add_argument ( '-fs', '--first_seed',      type=int, default=1,         help='the first seed in a series of seeds to run' )
    arg_parser.add_argument ( '-ls', '--last_seed',       type=int, default=1,         help='the last seed in a series of seeds to run' )
    arg_parser.add_argument ( '-lf', '--log_file_opt',    type=str, default='console', help='the log file option for mcell' )
    arg_parser.add_argument ( '-ef', '--error_file_opt',  type=str, default='console', help='the error file option for mcell' )
    arg_parser.add_argument ( '-np', '--num_processors',  type=int, default=8,         help='the number of processors' )
    arg_parser.add_argument ( '-rl', '--run_limit',       type=int, default=-1,        help='limit the total number of runs' )
    arg_parser.add_argument ( '-rt', '--runner_type',     type=str, default='mpp',     help='run mechanism: mpp or sge (mpp=MultiProcessingPool, sge=SunGridEngine)' )
    arg_parser.add_argument ( '-nl', '--node_list',       type=str, default='',        help='list of comma-separated nodes to run on with SGE' )
    arg_parser.add_argument ( '-mm', '--min_memory',      type=int, default=0,         help='minimum memory in Gigabytes' )
    arg_parser.add_argument ( '-em', '--email_addr',      type=str, default='',        help='email address for notifications of job results' )
    arg_parser.add_argument ( '-gh', '--grid_host',       type=str, default='',        help='grid engine host name' )
  """

  #__import__('code').interact(local={k: v for ns in (globals(), locals()) for k, v in ns.items()})

  fs = data_model['simulation_control']['start_seed']
  ls = data_model['simulation_control']['end_seed']

  run_data_model_mcell_3r.run_mcell_sweep(['-pd',project_dir,'-b',parameter_dictionary['MCellR Path']['val'],'-fs',fs,'-ls',ls],data_model={'mcell':data_model})



  # Return a list of run command dictionaries.
  # Each run command dictionary must contain a "cmd" key, an "args" key, and a "wd" key.
  # The cmd key will refer to a command string suitable for popen.
  # The args key will refer to an argument list suitable for popen.
  # The wd key will refer to a working directory string.
  # Each run command dictionary may contain any other keys helpful for post-processing.
  # The run command dictionary list will be passed on to the postprocess_runs function.

  # The data_layout should be a dictionary something like this:

  #  {
  #   "version": 2,
  #   "data_layout": [
  #    ["/DIR", ["output_data"]],
  #    ["dc_a", [1e-06, 1e-05]],
  #    ["nrel", [100.0, 200.0, 300.0]],
  #    ["/FILE_TYPE", ["react_data", "viz_data"]],
  #    ["/SEED", [100, 101]]
  #   ]
  #  }

  # That dictionary describes the directory structure that CellBlender expects to find on the disk

  command_list = []

  output_detail = parameter_dictionary['Output Detail (0-100)']['val']

  if output_detail > 0: print ( "Inside MCellR Engine, project_dir=" + project_dir )

  return ( command_list )


def postprocess_runs ( data_model, command_strings ):
  # Move and/or transform data to match expected CellBlender file structure as required
  pass


if __name__ == "__main__":
    print ( "Called with __name__ == __main__" )
    pass