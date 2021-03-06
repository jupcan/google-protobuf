# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import exercise_pb2 as exercise__pb2


class IdentStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.getID = channel.unary_unary(
        '/exercise.Ident/getID',
        request_serializer=exercise__pb2.GetIdRequest.SerializeToString,
        response_deserializer=exercise__pb2.GetIdReply.FromString,
        )


class IdentServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def getID(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_IdentServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'getID': grpc.unary_unary_rpc_method_handler(
          servicer.getID,
          request_deserializer=exercise__pb2.GetIdRequest.FromString,
          response_serializer=exercise__pb2.GetIdReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'exercise.Ident', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class CheckStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.checkme = channel.unary_unary(
        '/exercise.Check/checkme',
        request_serializer=exercise__pb2.CheckmeRequest.SerializeToString,
        response_deserializer=exercise__pb2.CheckmeReply.FromString,
        )


class CheckServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def checkme(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CheckServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'checkme': grpc.unary_unary_rpc_method_handler(
          servicer.checkme,
          request_deserializer=exercise__pb2.CheckmeRequest.FromString,
          response_serializer=exercise__pb2.CheckmeReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'exercise.Check', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
