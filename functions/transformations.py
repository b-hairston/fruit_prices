
import polars as pl
import pydantic
from pydantic import BaseModel, field_validator, ValidationError, ValidationInfo




# pydnatic model for the input file
class AggFruitPrices(BaseModel):
    FRUIT: str
    FORM: str
    RETAIL_PRICE: float
    RETAIL_PRICE_UNIT: str
    YIELD: float
    CUP_EQUIVALENT_SIZE: float
    CUP_EQUIVALENT_UNIT: str
    CUP_EQUIVALENT_PRICE: float
    
class IndvFruitPrices(BaseModel):
    FORM: str
    AVERAGE_RETAIL_PRICE: float
    PREPARATION_YEILD_FACTOR: float
    SIZE_OF_CUP_EQUIVALENT: float
    AVERAGE_PRICE_PER_CUP_EQUIVALENT: float
    
    
def normalize_csv(input_file):
    df = pl.read_csv(input_file, skip_rows=1)
    # Normalize the column names
    
    print(df)
    
    
normalize_csv("prices/broccoli 2016.csv")