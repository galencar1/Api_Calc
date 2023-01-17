from pydantic import BaseModel, Field


class OperationRequest(BaseModel):
    n1: int = Field(
        None, title="Operando 1", description="Variável para execução da operação"
    )
    n2: int = Field(
        None, title="Operando 2", description="Variável para execução da operação"
    )
