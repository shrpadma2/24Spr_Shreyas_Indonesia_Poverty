#%%
import json
import os
import shutil

#%%

def save_to_json(data, output_file_path):
    with open(output_file_path, 'w') as output_file:
        json.dump(data, output_file, indent=2)

semester2code = { "sp":"01", "spr":"01", "spring":"01", "su":"02", "sum":"02", "summer":"02", "fa":"03", "fall":"03"}
thisfilename = os.path.basename(__file__) # should match _ver for version, ideally 3-digit string starting as "000", up to "999"

data_to_save = \
    {
        # -----------------------------------------------------------------------------------------------------------------------
        "Version":
            """001""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Year":
            """2024""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Semester":
            """Spring""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """Indonesia Poverty and Equity Program""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Objective":
            """ 
            The primary objective of this project is to leverage various datasets, including AIS (shipping transponder) data, 
            household surveys, and census data, to gain comprehensive insights into the spatial transformation and connectivity 
            within Indonesia. By analyzing these datasets, the project aims to identify key patterns, challenges, and opportunities
            in the structural transformation of Indonesia, focusing on aspects that directly impact the well-being and economic 
            equity of its population. The goal is to develop actionable strategies and policy recommendations that will facilitate 
            improved connectivity and equitable growth across different regions of Indonesia. This analysis will ultimately contribute 
            to a better understanding of how spatial transformation influences poverty reduction and equitable development, thereby 
            supporting the broader objective of improving the living standards and opportunities for the people of Indonesia.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Dataset":
            """
            William Hutchins Seitz has provided the data, and the subsequent details offer an explanation of the shared data.

            The Indonesia EAP project encompasses a rich array of socio-economic, health, and educational data, spanning multiple administrative 
            levels from villages (desa) to regencies (kabupaten), primarily derived from the PODES surveys and related data collection efforts. 
            This extensive dataset, with information from different years, including 2011 and 2019, offers a detailed snapshot of Indonesia's regional development, 
            demographic trends, healthcare and educational infrastructure, and socio-economic conditions. The depth and breadth of the data provide a unique opportunity
            for in-depth analysis, critical for informed policy-making, targeted developmental initiatives, and comprehensive academic research, aimed at understanding
            and addressing Indonesia's regional disparities and enhancing welfare outcomes.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Rationale":
            """
            The Indonesia EAP Project aims to improve welfare outcomes by using its data to identify and tackle regional disparities in healthcare, education, and socio-economic conditions.
            This targeted approach is intended to reduce inequalities and enhance the overall quality of life across Indonesia, leading to more equitable and inclusive development.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Approach":
            """
            Our team plans to tackle this capstone project through a series of coordinated steps:

            1. Gain a thorough understanding of the data and carry out the necessary preprocessing.
            2. With multiple datasets at our disposal, we will merge them to achieve a comprehensive view of poverty and consumption patterns.
            3. We will then integrate satellite data with survey data and proceed with the required statistical modeling.
            4. The team will engage in visualization and mapping to create graphical representations of our findings.
            5. Lastly, we will validate our findings to ensure the reliability and robustness of our models.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Timeline":
            """
            This a rough time line for this project:  

            - (2 Weeks) Data Pre-Processing.  
            - (1 Weeks) Consolidation and Aggregation
            - (2 Weeks) Satellite & GIS Data Integration 
            - (2 Weeks) Survey Data and Satelitte Data Merging  
            - (3 Weeks) Statistical Modelling
            - (2 Weeks) Visualization and Mapping
            - (1 Weeks) Validation  
            - (1 Weeks) Writing Up a paper and submission
            - (1 Weeks) Final Presentation  
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Expected Number Students":
            """
            2 People 
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Possible Issues":
            """
           The challenge involves comprehending the survey data, preparing and processing this data, and then integrating it effectively with satellite and GIS data.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Proposed by": "William Seitz",
        "Proposed by email": "wseitz@worldbank.org",
        "instructor": "Edwin Lo",
        "instructor_email": "edwinlo@email.gwu.edu",
        "github_repo": "https://github.com/shrpadma2/DATS_6501_10_Capstone_Project",
        # -----------------------------------------------------------------------------------------------------------------------
    }
os.makedirs(
    os.getcwd() + f'{os.sep}Proposals{os.sep}{data_to_save["Year"]}{semester2code[data_to_save["Semester"].lower()]}{os.sep}{data_to_save["Version"]}',
    exist_ok=True)
output_file_path = os.getcwd() + f'{os.sep}Proposals{os.sep}{data_to_save["Year"]}{semester2code[data_to_save["Semester"].lower()]}{os.sep}{data_to_save["Version"]}{os.sep}'
save_to_json(data_to_save, output_file_path + "input.json")
shutil.copy(thisfilename, output_file_path)
print(f"Data saved to {output_file_path}")
