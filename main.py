from fastapi import FastAPI
from thread import DataUploadThread

# Instantiate the class
app = FastAPI()

# Define a GET method on the specified endpoint

@app.post("/branch_id={branch_id}&variant_id={variant_id}&number_of_codes={number_of_codes}&cd_id={cd_id}")
async def generate_code(branch_id: int, variant_id: int, number_of_codes : int, cd_id:int):
    #Use Thread to Generate Codes in the Background
    DataUploadThread(branch_id,variant_id,number_of_codes,cd_id).start()
    #create response body
    context = {"status":True,"message":"Success"}
    #return response body
    return context
