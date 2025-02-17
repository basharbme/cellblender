pbc_dm = {
  'model_language': 'mcell3',
  'api_version' : 0,
  'blender_version' : [2, 78, 0],
  'cellblender_source_sha1' : "deae7bc4e7997d7a9a9efe8c6fde29a17d866c61",
  'cellblender_version' : "0.1.54",
  'data_model_version' : "DM_2014_10_24_1638",
  'define_molecules' : {
    'data_model_version' : "DM_2014_10_24_1638",
    'molecule_list' : [
      {
        'custom_space_step' : "",
        'custom_time_step' : "",
        'data_model_version' : "DM_2016_01_13_1930",
        'diffusion_constant' : "1e-6",
        'display' : {
          'color' : [1.0, 0.0, 0.0],
          'emit' : 0.0,
          'glyph' : "Sphere_1",
          'scale' : 1.0
        },
        'export_viz' : False,
        'maximum_step_length' : "",
        'mol_bngl_label' : "",
        'mol_name' : "vm",
        'mol_type' : "3D",
        'target_only' : False
      }
    ]
  },
  'define_reactions' : {
    'data_model_version' : "DM_2014_10_24_1638",
    'reaction_list' : []
  },
  'define_release_patterns' : {
    'data_model_version' : "DM_2014_10_24_1638",
    'release_pattern_list' : []
  },
  'define_surface_classes' : {
    'data_model_version' : "DM_2014_10_24_1638",
    'surface_class_list' : [
      {
        'data_model_version' : "DM_2014_10_24_1638",
        'name' : "transp",
        'surface_class_prop_list' : [
          {
            'affected_mols' : "ALL_MOLECULES",
            'clamp_value' : "0",
            'data_model_version' : "DM_2015_11_08_1756",
            'molecule' : "",
            'name' : "Molec.: ALL_MOLECULES   Orient.: Ignore   Type: Transparent",
            'surf_class_orient' : ";",
            'surf_class_type' : "TRANSPARENT"
          }
        ]
      }
    ]
  },
  'geometrical_objects' : {
    'object_list' : [
      {
        'element_connections' : [
          [2, 3, 1],
          [2, 0, 3]
        ],
        'location' : [0.0, 0.0, 0.0],
        'material_names' : ['plane_mat'],
        'name' : "plane",
        'vertex_list' : [
          [0.0, -0.10999999940395355, -0.10999999940395355],
          [0.0, 0.10999999940395355, 0.10999999940395355],
          [0.0, -0.10999999940395355, 0.10999999940395355],
          [0.0, 0.10999999940395355, -0.10999999940395355]
        ]
      },
      {
        'element_connections' : [
          [1, 2, 0],
          [3, 6, 2],
          [7, 4, 6],
          [5, 0, 4],
          [6, 0, 2],
          [3, 5, 7],
          [1, 3, 2],
          [3, 7, 6],
          [7, 5, 4],
          [5, 1, 0],
          [6, 4, 0],
          [3, 1, 5]
        ],
        'location' : [0.0, 0.0, 0.0],
        'material_names' : ['sampling_box_mat'],
        'name' : "sampling_box",
        'vertex_list' : [
          [-0.49900001287460327, -0.0989999771118164, -0.0989999771118164],
          [-0.49900001287460327, -0.0989999771118164, 0.09900002181529999],
          [-0.49900001287460327, 0.0989999771118164, -0.0989999771118164],
          [-0.49900001287460327, 0.0989999771118164, 0.09900002181529999],
          [-0.0010000000474974513, -0.0989999771118164, -0.0989999771118164],
          [-0.0010000000474974513, -0.0989999771118164, 0.09900002181529999],
          [-0.0010000000474974513, 0.0989999771118164, -0.0989999771118164],
          [-0.0010000000474974513, 0.0989999771118164, 0.09900002181529999]
        ]
      }
    ]
  },
  'initialization' : {
    'accurate_3d_reactions' : True,
    'center_molecules_on_grid' : False,
    'data_model_version' : "DM_2014_10_24_1638",
    'interaction_radius' : "",
    'iterations' : "1000",
    'microscopic_reversibility' : "OFF",
    'notifications' : {
      'all_notifications' : "INDIVIDUAL",
      'box_triangulation_report' : False,
      'diffusion_constant_report' : "BRIEF",
      'file_output_report' : False,
      'final_summary' : True,
      'iteration_report' : True,
      'molecule_collision_report' : False,
      'partition_location_report' : False,
      'probability_report' : "ON",
      'probability_report_threshold' : "0",
      'progress_report' : True,
      'release_event_report' : True,
      'varying_probability_report' : True
    },
    'partitions' : {
      'data_model_version' : "DM_2016_04_15_1600",
      'include' : False,
      'recursion_flag' : False,
      'x_end' : "1",
      'x_start' : "-1",
      'x_step' : "0.02",
      'y_end' : "1",
      'y_start' : "-1",
      'y_step' : "0.02",
      'z_end' : "1",
      'z_start' : "-1",
      'z_step' : "0.02"
    },
    'radial_directions' : "",
    'radial_subdivisions' : "",
    'space_step' : "",
    'surface_grid_density' : "10000",
    'time_step' : "1e-6",
    'time_step_max' : "",
    'vacancy_search_distance' : "",
    'warnings' : {
      'all_warnings' : "INDIVIDUAL",
      'degenerate_polygons' : "WARNING",
      'high_probability_threshold' : "1",
      'high_reaction_probability' : "IGNORED",
      'lifetime_threshold' : "50",
      'lifetime_too_short' : "WARNING",
      'missed_reaction_threshold' : "0.001",
      'missed_reactions' : "WARNING",
      'missing_surface_orientation' : "ERROR",
      'negative_diffusion_constant' : "WARNING",
      'negative_reaction_rate' : "WARNING",
      'useless_volume_orientation' : "WARNING"
    }
  },
  'materials' : {
    'material_dict' : {
      'plane_mat' : {
        'diffuse_color' : {
          'a' : 0.25,
          'b' : 0.800000011920929,
          'g' : 0.800000011920929,
          'r' : 0.800000011920929
        }
      },
      'sampling_box_mat' : {
        'diffuse_color' : {
          'a' : 0.25,
          'b' : 0.800000011920929,
          'g' : 0.800000011920929,
          'r' : 0.800000011920929
        }
      }
    }
  },
  'model_objects' : {
    'data_model_version' : "DM_2014_10_24_1638",
    'model_object_list' : [
      {
        'name' : "plane"
      },
      {
        'name' : "sampling_box"
      }
    ]
  },
  'modify_surface_regions' : {
    'data_model_version' : "DM_2014_10_24_1638",
    'modify_surface_regions_list' : [
      {
        'data_model_version' : "DM_2015_11_06_1732",
        'name' : "Surface Class: transp   Object: sampling_box   ALL",
        'object_name' : "sampling_box",
        'region_name' : "",
        'region_selection' : "ALL",
        'surf_class_name' : "transp"
      }
    ]
  },
  'mol_viz' : {
    'active_seed_index' : 0,
    'color_index' : 0,
    'color_list' : [
      [0.800000011920929, 0.0, 0.0],
      [0.0, 0.800000011920929, 0.0],
      [0.0, 0.0, 0.800000011920929],
      [0.0, 0.800000011920929, 0.800000011920929],
      [0.800000011920929, 0.0, 0.800000011920929],
      [0.800000011920929, 0.800000011920929, 0.0],
      [1.0, 1.0, 1.0],
      [0.0, 0.0, 0.0]
    ],
    'data_model_version' : "DM_2015_04_13_1700",
    'file_dir' : "",
    'file_index' : 0,
    'file_name' : "Scene.cellbin.0000.dat",
    'file_num' : 1001,
    'file_start_index' : 0,
    'file_step_index' : 1,
    'file_stop_index' : 1000,
    'manual_select_viz_dir' : False,
    'render_and_save' : False,
    'seed_list' : ['seed_00001'],
    'viz_enable' : True,
    'viz_list' : ['mol_vm']
  },
  'parameter_system' : {
    'model_parameters' : [],
  },
  'reaction_data_output' : {
    'always_generate' : True,
    'combine_seeds' : True,
    'data_model_version' : "DM_2016_03_15_1800",
    'mol_colors' : False,
    'output_buf_size' : "",
    'plot_layout' : " plot ",
    'plot_legend' : "0",
    'reaction_output_list' : [
      {
        'count_location' : "World",
        'data_file_name' : "",
        'data_model_version' : "DM_2016_03_15_1800",
        'mdl_file_prefix' : "",
        'mdl_string' : "",
        'molecule_name' : "vm",
        'name' : "Count vm in World",
        'object_name' : "",
        'plotting_enabled' : True,
        'reaction_name' : "",
        'region_name' : "",
        'rxn_or_mol' : "Molecule"
      },
      {
        'count_location' : "Object",
        'data_file_name' : "",
        'data_model_version' : "DM_2016_03_15_1800",
        'mdl_file_prefix' : "",
        'mdl_string' : "",
        'molecule_name' : "vm",
        'name' : "Count vm in/on sampling_box",
        'object_name' : "sampling_box",
        'plotting_enabled' : True,
        'reaction_name' : "",
        'region_name' : "",
        'rxn_or_mol' : "Molecule"
      }
    ],
    'rxn_step' : ""
  },
  'release_sites' : {
    'data_model_version' : "DM_2014_10_24_1638",
    'release_site_list' : [
      {
        'data_model_version' : "DM_2015_11_11_1717",
        'location_x' : ".495",
        'location_y' : "0",
        'location_z' : "0",
        'molecule' : "vm",
        'name' : "rel_vm",
        'object_expr' : "",
        'orient' : "'",
        'pattern' : "",
        'points_list' : [],
        'quantity' : "1000",
        'quantity_type' : "NUMBER_TO_RELEASE",
        'release_probability' : "1",
        'shape' : "SPHERICAL",
        'site_diameter' : "0",
        'stddev' : "0"
      }
    ]
  },
  'scripting' : {
    'data_model_version' : "DM_2016_03_15_1900",
    'dm_external_file_name' : "",
    'dm_internal_file_name' : "",
    'force_property_update' : True,
    'script_texts' : {
      'pbc.mdl' : """PERIODIC_BOX
{
  CORNERS = [-0.5, -0.1, -0.1],[0.5, 0.1, 0.1]
  PERIODIC_TRADITIONAL = TRUE
  PERIODIC_X = TRUE
  PERIODIC_Y = TRUE
  PERIODIC_Z = TRUE
}"""
    },
    'scripting_list' : [
      {
        'data_model_version' : "DM_2016_03_15_1900",
        'external_file_name' : "",
        'include_section' : "initialization",
        'include_where' : "before",
        'internal_external' : "internal",
        'internal_file_name' : "pbc.mdl",
        'mdl_python' : "mdl",
        'name' : ""
      }
    ],
    'show_data_model_scripting' : True,
    'show_simulation_scripting' : True
  },
  'simulation_control' : {
    'data_model_version' : "DM_2016_10_27_1642",
    'end_seed' : "1",
    'name' : "",
    'processes_list' : [
      {
        'data_model_version' : "DM_2015_04_23_1753",
        'name' : "PID: 31191, MDL: Scene.main.mdl, Seed: 1"
      },
      {
        'data_model_version' : "DM_2015_04_23_1753",
        'name' : "PID: 31861, MDL: Scene.main.mdl, Seed: 1"
      },
      {
        'data_model_version' : "DM_2015_04_23_1753",
        'name' : "PID: 6126, MDL: Scene.main.mdl, Seed: 1"
      },
      {
        'data_model_version' : "DM_2015_04_23_1753",
        'name' : "PID: 10338, MDL: Scene.main.mdl, Seed: 1"
      },
      {
        'data_model_version' : "DM_2015_04_23_1753",
        'name' : "PID: 12644, MDL: Scene.main.mdl, Seed: 1"
      }
    ],
    'run_limit' : "-1",
    'start_seed' : "1"
  },
  'viz_output' : {
    'all_iterations' : True,
    'data_model_version' : "DM_2014_10_24_1638",
    'end' : "1",
    'export_all' : True,
    'start' : "0",
    'step' : "1"
  }
}
