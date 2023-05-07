import csv
from django.http import HttpResponse


def export_to_csv(modelAdmin, request, queryset):
    # Create the HttpResponse object with CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(modelAdmin.model.__name__)

    # Create the CSV writer
    writer = csv.writer(response)

    # Write header row
    header = [field.name for field in modelAdmin.model._meta.fields]
    writer.writerow(header)

    # Write data rows
    for obj in queryset:
        # Get the value of each field for the current object, and add it to the row
        row = [getattr(obj, field.name) for field in modelAdmin.model._meta.fields]
        writer.writerow(row)

    return response


export_to_csv.short_description = "Export to CSV"
