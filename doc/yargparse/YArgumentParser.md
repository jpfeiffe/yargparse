Module yargparse.YArgumentParser
================================

Functions
---------

    
`dicts_to_namespaces(config) -> argparse.Namespace`
:   Translate a dictionary of dictionaries to namespaces of namespaces.  Recursively calls itself until reaching the basecase of not being a 
    dictionary, then returns the value at the leaf

Classes
-------

`YArgumentParser(yaml_flag='-c', yaml_dest='--config', yaml_default='config.yaml', **kwargs)`
:   Layer over argparse that merges YAML configuration with command line overrides.
    
    Allows some variables to be defined at the CLI, and others to be in the YAML.  CLI will always override
    defaults provided in YAML, if provided in both places.
    
    To override nested YAML use dot notation, e.g.:
    features
        dim: 100
    
    can be overridden via --features.dim 1000
    
    Initialization including specifying the desired YAML file to use in command line interface.
    
    Example CLI: python <prog> -c / --config config.yaml
    
    yaml_flag: the one-dash command line shortcut (e.g., -c)
    yaml_dest: the two-dash command line arg (e.g., --config)
    yaml_default: Default value (e.g., config.yaml)

    ### Ancestors (in MRO)

    * argparse.ArgumentParser
    * argparse._AttributeHolder
    * argparse._ActionsContainer

    ### Methods

    `parse_args(self, args=None) -> argparse.Namespace`
    :   Overrides argparse's parse_args, to first recover the yaml configuration file and other true CLI,
        then merges the other CLI with the YAML file.
        
        Lastly, it combines both into a dict, which is translated into a namespace