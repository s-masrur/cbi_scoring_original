import json


def create_validator(dataset_df, target_col_name, filename):
    validator = {
        'title': 'ScoreModel',
        'type': 'object',
        'properties': {

        },
        'required': [

        ]
    }

    for col in dataset_df:
        if col == target_col_name:
            continue
        if dataset_df[col].dtype == 'O':
            choices = {
                'enum': list(dataset_df[col].unique()),
                'type': 'string'
            }
            validator['properties'][col] = choices
        elif dataset_df[col].dtype == 'int64':
            maxmin = {
                'maximum': int(dataset_df[col].max()),
                'minimum': int(dataset_df[col].min()),
                'type': 'integer'
            }
            validator['properties'][col] = maxmin
        elif dataset_df[col].dtype == 'float64':
            maxmin = {
                'maximum': float(dataset_df[col].max()),
                'minimum': float(dataset_df[col].min()),
                'type': 'number'
            }
            validator['properties'][col] = maxmin

        validator['required'].append(col)

    with open(filename+'.json', 'w') as file:
        file.write(json.dumps(validator))

