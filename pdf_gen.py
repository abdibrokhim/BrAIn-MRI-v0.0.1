from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(patient_name, birth_year, observation_date, doctor_name, observation, conclusion, head_doctor_name, file_path='report.pdf'):
    """
    Generate a PDF report for the MRI study of the brain.
    """

    try:
        # Set up the PDF document
        doc = SimpleDocTemplate(file_path, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        # Add patient information
        story.append(Paragraph(f'<b>Patient name:</b> {patient_name}', styles['Normal']))
        story.append(Paragraph(f'<b>Birth year:</b> {birth_year}', styles['Normal']))
        story.append(Paragraph(f'<b>Observation date:</b> {observation_date}', styles['Normal']))
        story.append(Paragraph(f'<b>Observed by:</b> {doctor_name}', styles['Normal']))
        story.append(Spacer(1, 12))

        # Add heading
        story.append(Paragraph('PROTOCOL OF MRI STUDY OF THE BRAIN', styles['Heading1']))
        story.append(Spacer(1, 12))

        # Add observation and conclusion
        story.append(Paragraph('<b>Observation:</b>', styles['Normal']))
        story.append(Paragraph(observation, styles['Normal']))
        story.append(Spacer(1, 12))
        story.append(Paragraph('<b>Conclusion:</b>', styles['Normal']))
        story.append(Paragraph(conclusion, styles['Normal']))
        story.append(Spacer(1, 12))

        # Add signature
        story.append(Paragraph(f'Signed by: {head_doctor_name}', styles['Normal']))

        # Build the PDF
        doc.build(story)

        return file_path
    except Exception as e:
        return f"An error occurred: {str(e)}"


# # Sample usage
# if __name__ == '__main__':
#     generate_pdf(
#         patient_name='John Doe',
#         birth_year='1985',
#         observation_date='15.02.2024',
#         doctor_name='Dr. Smith',
#         observation='Multiple sclerosis',
#         conclusion='Early signs of multiple sclerosis',
#         head_doctor_name='Dr. Johnson'
#     )
