#https://stackoverflow.com/questions/61140398/fastapi-return-a-file-response-with-the-output-of-a-sql-query
from fastapi.responses import StreamingResponse
import io
    
@app.get("/get_csv")
async def get_csv():

    df = pandas.DataFrame(dict(col1 = 1, col2 = 2))

    stream = io.StringIO()

    df.to_csv(stream, index = False)

    response = StreamingResponse(iter([stream.getvalue()]),
                        media_type="text/csv"
    )

    response.headers["Content-Disposition"] = "attachment; filename=export.csv"

    return response