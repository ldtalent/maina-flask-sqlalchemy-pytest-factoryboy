from marshmallow import Schema, fields, validate, ValidationError, post_load

class TodoSchema(Schema):
    
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    completed = fields.Bool()
    from_date = fields.DateTime()
    to_date = fields.DateTime()
    

    @post_load(pass_many=True)
    def _check_dates_validity(self, in_data, **kwargs):
        if in_data["from_date"] > in_data["to_date"]:
            raise ValidationError("from_date cannot be later than to_date")
        return in_data

class TodosEditSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    completed = fields.Bool()
    from_date = fields.DateTime()
    to_date = fields.DateTime()

    @post_load(pass_many=True)
    def _check_dates_validity(self, in_data, **kwargs):
        if "from_date" in in_data.keys() and "to_date" in in_data.keys():
            if in_data["from_date"] > in_data["to_date"]:
                raise ValidationError("from_date cannot be later than to_date")
        return in_data