from typing import Optional
from google.api_core.client_options import ClientOptions
from google.cloud import documentai  # type: ignore
from google.protobuf.field_mask_pb2 import FieldMask  # Import FieldMask
from google.protobuf.json_format import MessageToJson  # Import MessageToJson

def parseInvoice():
    def process_document_sample(
        project_id: str = "oos-invoice-processing-415721",
        location: str = "us",
        processor_id: str = "e5dc600a9a70dbea",
        file_path: str = r"C:\Users\Ztrei\OneDrive\Documents\Programming Projects\OoS Invoice Project\OoS-Invoice-Project\IMG_2614_rotated.pdf",
        mime_type: str = "application/pdf",
        field_mask: Optional[list] = ["text", "entities", "Invoice-Brand","Invoice-row"],
        processor_version_id: Optional[str] = "1fe386d94daf6048"  # Use the version ID here
    ) -> None:
        opts = ClientOptions(api_endpoint=f"us-documentai.googleapis.com")

        client = documentai.DocumentProcessorServiceClient(client_options=opts)

        if processor_version_id:
            name = client.processor_version_path(project_id, location, processor_id, processor_version_id)
        else:
            name = client.processor_path(project_id, location, processor_id)

        with open(file_path, "rb") as image:
            image_content = image.read()

        process_options = documentai.ProcessOptions(
            individual_page_selector=documentai.ProcessOptions.IndividualPageSelector(
                pages=[1]
            )
        )

        raw_document = documentai.RawDocument(content=image_content, mime_type=mime_type)

        field_mask_obj = FieldMask(paths=field_mask)
        request = documentai.ProcessRequest(
            name=name,
            raw_document=raw_document,
            field_mask=field_mask_obj,
            process_options=process_options,
        )

        result = client.process_document(request=request)
        document = result.document

        # Access and write entities to a .txt file if requested
        if "entities" in field_mask:
            entities = document.entities
            # Open a file to write the output
            with open("invoice_output.txt", "w", encoding='utf-8', errors='ignore') as file:
                for entity in entities:
                    if entity.type_ == "Invoice-Brand":
                        file.write(f"Invoice Brand: {entity.mention_text}\n")  # Write the Invoice Brand to the file

                for entity in entities:
                    if entity.type_ == "Invoice-row":
                        file.write(f"Item: {entity.mention_text}\n")  # Write the Invoice row item to the file

    # Call the function
    process_document_sample()
