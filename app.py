import streamlit as st
from api import generate_response
from db import *
from pdf_gen import generate_pdf
import uuid
import time


# Set page title
st.title("BrAIn MRI")

# Create sidebar for tabs
selected_tab = st.sidebar.radio("Navigation", ["Observation", "Conclusions"])

res = ""


def generate_key(record_id):
    # Generate a random UUID
    random_uuid = str(uuid.uuid4()).replace('-', '')

    # Get current timestamp
    current_time = str(int(time.time()))

    # Concatenate UUID and timestamp
    key = random_uuid + current_time + str(record_id)

    return key

# Display content based on selected tab
if selected_tab == "Observation":
    # Add a dropdown menu for options
    option = st.selectbox("Select an Option", ["", "Brain", "FuturePlans"], format_func=lambda x: 'Select an Option' if x == '' else x, key='option', 
                          help='Choose the desired option')

    # Display content based on selected option
    if option == "Brain":
        st.write("You selected Brain option.")
        scanning_technique = st.text_input("Scanning Technique:")
        
        st.subheader("Basal Ganglia")
        basal_ganglia_location = st.text_input("Location:")
        basal_ganglia_symmetry = st.text_input("Symmetry:")
        basal_ganglia_contour = st.text_input("Contour:")
        basal_ganglia_dimensions = st.text_input("Dimensions:")
        basal_ganglia_signal = st.text_input("MR Signal:")
        
        st.subheader("Brain Grooves and Ventricles")
        lateral_ventricles_width_right = st.number_input("Right Lateral Ventricles Width (mm):", min_value=0)
        lateral_ventricles_width_left = st.number_input("Left Lateral Ventricles Width (mm):", min_value=0)
        third_ventricle_width = st.number_input("Third Ventricle Width (mm):", min_value=0)
        sylvian_aqueduct_condition = st.text_input("Condition of Sylvian Aqueduct:")
        fourth_ventricle_condition = st.text_input("Condition of Fourth Ventricle:")
        
        st.subheader("Brain Structures")
        corpus_callosum_condition = st.text_input("Corpus Callosum:")
        brain_stem_condition = st.text_input("Brain Stem:")
        cerebellum_condition = st.text_input("Cerebellum:")
        craniovertebral_junction_condition = st.text_input("Craniovertebral Junction:")
        pituitary_gland_condition = st.text_input("Pituitary Gland:")
        
        st.subheader("Optic Nerves and Orbital Structures")
        orbital_cones_shape = st.text_input("Orbital Cones Shape:")
        eyeballs_shape_size = st.text_input("Eyeballs Shape and Size:")
        optic_nerves_diameter = st.number_input("Optic Nerves Diameter (mm):", min_value=0)
        extraocular_muscles_condition = st.text_input("Extraocular Muscles:")
        retrobulbar_fatty_tissue_condition = st.text_input("Retrobulbar Fatty Tissue:")
        
        st.subheader("Paranasal Sinuses")
        sinuses_cysts_presence = st.radio("Cysts Presence in Paranasal Sinuses:", options=["Yes", "No"])
        sinuses_cysts_size = st.number_input("Cysts Size (mm):", min_value=0)
        sinuses_pneumatization = st.text_input("Sinuses Pneumatization:")
        
        additional_observations = st.text_area("Additional Observations:")

        name = st.text_input("Patient Full Name:")
        year = st.text_input("Patient Birth Year:")
        radiologist_name = st.text_input("Radiologist Name:")
        
        if st.button("Generate"):
            # template = f"""
            # Here is the information from the observations to update the template:
            # - Scanning Technique: {scanning_technique}
            # - Basal Ganglia: (Heading)
            #   - Location: {basal_ganglia_location}
            #   - Symmetry: {basal_ganglia_symmetry}
            #   - Contour: {basal_ganglia_contour}
            #   - Dimensions: {basal_ganglia_dimensions}
            #   - MR Signal: {basal_ganglia_signal}
            # - Brain Grooves and Ventricles: (Heading)
            #   - Lateral Ventricles Width: Right: {lateral_ventricles_width_right} mm, Left: {lateral_ventricles_width_left} mm
            #   - Third Ventricle Width: {third_ventricle_width} mm
            #   - Sylvian Aqueduct: {sylvian_aqueduct_condition}
            #   - Fourth Ventricle: {fourth_ventricle_condition}
            # - Brain Structures: (Heading)
            #   - Corpus Callosum: {corpus_callosum_condition}
            #   - Brain Stem: {brain_stem_condition}
            #   - Cerebellum: {cerebellum_condition}
            #   - Craniovertebral Junction: {craniovertebral_junction_condition}
            #   - Pituitary Gland: Normal shape, height 4{pituitary_gland_condition} mm in sagittal projection
            # - Optic Nerves and Orbital Structures: (Heading)
            #   - Orbital Cones Shape: {orbital_cones_shape}
            #   - Eyeballs Shape and Size: {eyeballs_shape_size}
            #   - Optic Nerves Diameter: {optic_nerves_diameter}
            #   - Extraocular Muscles: {extraocular_muscles_condition}
            #   - Retrobulbar Fatty Tissue: {retrobulbar_fatty_tissue_condition}
            # - Paranasal Sinuses: (Heading)
            #   - Cysts Presence: {sinuses_cysts_presence}
            #   - Cysts Size: {sinuses_cysts_size} mm
            #   - Sinuses Pneumatization: {sinuses_pneumatization}
            # - Additional Observations: {additional_observations}
            # """


# TESTING PURPOSES ONLY
            template = """
            - Scanning Technique: T1 FSE-sagittal, T2 FLAIR, T2 FSE-axial, T2 FSE-coronal
- Basal Ganglia:
  - Location: Usually located
  - Symmetry: Symmetrical
  - Contour: Clear, even contours
  - Dimensions: Not changed
  - MR Signal: Not changed
- Brain Grooves and Ventricles:
  - Lateral Ventricles Width: Right: 7 mm, Left: 9 mm
  - Third Ventricle Width: 4 mm
  - Sylvian Aqueduct: Not changed
  - Fourth Ventricle: Tent-shaped and not dilated
- Brain Structures:
  - Corpus Callosum: Normal shape and size
  - Brain Stem: Without features
  - Cerebellum: Normal shape
  - Craniovertebral Junction: Unchanged
  - Pituitary Gland: Normal shape, height 4 mm in sagittal projection
- Optic Nerves and Orbital Structures:
  - Orbital Cones Shape: Unchanged
  - Eyeballs Shape and Size: Spherical and normal size
  - Optic Nerves Diameter: Preserved
  - Extraocular Muscles: Normal size, without pathological signals
  - Retrobulbar Fatty Tissue: Without pathological signals
- Paranasal Sinuses:
  - Cysts Presence: Not mentioned
  - Cysts Size: Not mentioned
  - Sinuses Pneumatization: Usually pneumatized
- Additional Observations: None mentioned
            """


            res = generate_response(template)
            # TESTING PURPOSES ONLY
            # res = "MRI signs of vascular encephalopathy with the presence of multiple small ischemic foci and atrophy of the frontotemporal areas on both sides."
            time.sleep(4)

            st.write("Conclusion:")
            st.markdown(res)

            data = {
                'full_name': name,
                'b_year': year,
                'observation': template,
                'conclusion': res,
                'radiologist_name': radiologist_name,
            }
            record_id = save_data(data)
            st.success(f'Data saved with ID: {record_id}')


    elif option == "FuturePlans":
        st.write("You selected FuturePlans option.")

elif selected_tab == "Conclusions":
    try:
        records = retrieve_all_data()
        print('records:', records)

        for record in records:
            record_data = {
                "Full Name": record['full_name'],
                "Birth Year": record['b_year'],
                "Observation": record['observation'],
                "Observation Date": record['observed_at'].strftime("%d.%m.%Y"),
                "Conclusion": record['conclusion'],
                "Radiologist Name": record['radiologist_name'],
                "Head Doctor Name": record['head_doctor_name'] if record['head_doctor_name'] else "N/A",
            }
            st.write("Record Details:")
            st.table(record_data)

            edit_button, delete_button, approve_button, pdf_button = st.columns(4)

            print(type(record['_id']))

            # Edit conclusion button
            if edit_button.button("Edit Conclusion"):
                new_conclusion = st.text_input("Enter new conclusion:", value=record['conclusion'])
                if st.button("Save") and new_conclusion:
                    r = update_data(record['_id'], {'conclusion': str(new_conclusion)})
                    print('update_data: ', r)
                    st.success("Conclusion updated successfully!")

            # Delete button
            if delete_button.button("Delete"):
                confirm = st.checkbox("Confirm deletion")
                if confirm:
                    delete_data(record['_id'])
                    st.success("Record deleted successfully!")
                    st.stop()

            # Approve button
            if not record['isApproved']:
                name = st.text_input("Enter Head doctor name:")
                if approve_button.button("Approve") and name:
                    update_approve_field(record['_id'], name)
                    st.success("Record approved successfully!")
                    st.stop()

            if pdf_button.button("Generate PDF"):
                file_path = generate_pdf(
                    patient_name=record['full_name'],
                    birth_year=record['b_year'],
                    observation_date=record['observed_at'].strftime("%d.%m.%Y"),
                    doctor_name=record['radiologist_name'],
                    observation=record['observation'],
                    conclusion=record['conclusion'],
                    head_doctor_name=record['head_doctor_name']
                )

                if file_path:
                    st.success("PDF report generated successfully!")
                    st.download_button(
                        label="Download PDF",
                        data=file_path,
                        file_name="report.pdf",
                        mime="application/pdf"
                    )
                    st.stop()


    except Exception as e:
        print('Error:', e)
        st.error("An error occurred while retrieving data from the database.")