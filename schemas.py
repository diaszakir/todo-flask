from marshmallow import Schema, fields

class PlainTaskSchema(Schema):
  id = fields.Int(dump_only=True) # We don't need that from user, but we will show it
  name = fields.Str(required=True)


class TaskSchema(PlainTaskSchema):
  status = fields.Str(load_default="Not started")


class TaskUpdateSchema(Schema):
  name = fields.Str(required=True)
  status = fields.Str(load_default="Not started") # load_default - for default values


class StatusUpdateSchema(Schema):
  status = fields.Str(required=True)