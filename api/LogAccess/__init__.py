import logging
import datetime
import uuid
import azure.functions as func
from azure.data.tables import TableServiceClient
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('LogAccess function triggered.')

    # Fecha y hora UTC
    timestamp = datetime.datetime.utcnow().isoformat()

    # Identificador único
    operation_id = str(uuid.uuid4())

    # Conexión a Azure Table Storage (usar configuración de la Function App)
    connection_string = os.environ["AzureWebJobsStorage"]
    table_service = TableServiceClient.from_connection_string(conn_str=connection_string)
    
    # Crear cliente de tabla (se crea si no existe)
    table_name = "AccessLogs"
    try:
        table_service.create_table(table_name=table_name)
    except Exception as e:
        logging.info(f"Table may already exist: {e}")


    table_client = table_service.get_table_client(table_name=table_name)

    # Entidad a guardar
    entity = {
        "PartitionKey": "Access", 
        "RowKey": operation_id,   
        "TimestampUTC": timestamp
    }

    # Insertar en la tabla
    table_client.upsert_entity(entity=entity)

    return func.HttpResponse(
        f"Access logged: {operation_id} at {timestamp}",
        status_code=200
    )
