from nicegui import ui 
import os
html_file_path = os.path.join(os.path.dirname(__file__), 'texte_essai.html')
texte_essai=open(html_file_path,'r', encoding='utf-8').read()

#Question
ui.markdown("## Aptitudes générales à la recherche ")


# creating slider 

# creating number 
#ui.number().bind_value(demo, 'number') 

# Initialize an empty list to store slider positions
slider_positions = [0] * 7

def save_positions():
    global slider_positions
    slider_positions = [slider.value for slider in sliders]
    ui.notify(f"Positions enregistrées: {slider_positions}")

# Create sliders list
sliders = []
questions=['Connaissances scientifiques générales',\
'Connaissances expertes dans son domaine de discipline',\
'Connaissances des techniques utilisées et résolution de problèmes dans la discipline',\
'Comprendre et justifier les objectifs du projet',\
'Intégration du projet dans la littérature scientifique',\
'Esprit critique',\
' “Think out of the box” ']



hover_text = ui.markdown('')
hover_text.style('margin-right: 20px; visibility: hidden;')

# compétences=[""" 
#     <div style="border:2px solid black; padding: 10px; background-color: #f0f0f0;">
#     <h6 style="color:blue;"> Base de connaissances dans plusieurs disciplines, acquise lors de cours, de séminaires, de clubs de lecture, etc.</h6>

#     <h6 style="color:green;"><i>Doctorant débutant</i> </h6>
#     <ul>
#         <li><strong>Faire l'état de l'art</strong> des nouvelles connaissances au-delà des frontières disciplinaires</li>
#     </ul>

#     <h6 style="color:purple;">Doctorant avancé</h6>

#     **Démontrer**, par ses réponses aux questions, une compréhension des nouvelles connaissances au-delà des frontières disciplinaires.

#     <h2 style="color:DarkBlue;">Doctorant diplômé</h2>

#     **Démontrer**, par la formulation de nouvelles questions, une compréhension des nouvelles données et des nouvelles connaissances au-delà des frontières disciplinaires.

#     \-----------------------------------------------

#     **Approches scientifiques générales**

#     *Doctorant débutant*

#     **Comprendre** les principes fondamentaux et les bases expérimentales de plusieurs disciplines

#     *Doctorant avancé*

#     **Poser des questions** pertinentes qui relient plusieurs disciplines au projet de recherche. 

#     *Doctorant diplômé*

#     **Intégre**r plusieurs disciplines dans la recherche </div>"""]*6 +\
#         ["""
#     <div style="border:2px solid black; padding: 10px; background-color: #f0f0f0;">
#     <h2 style="color:blue;">Base de connaissances dans plusieurs disciplines, acquise lors de cours, de séminaires, de clubs de lecture, etc.</h2>
#     <p style="font-size:14px;">This is a long text that needs to be displayed in a markdown format.</p>
    
#     <h2 style="color:green;">Subtitle</h2>
#     <p style="font-size:14px;">Here is some more text. This should be on a new line.</p>
    
#     <ul>
#         <li style="color:red; font-size:14px;">Bullet point 1</li>
#         <li style="color:red; font-size:14px;">Bullet point 2</li>
#     </ul>
    
#     <h3 style="color:purple;">Subsubtitle</h3>
#     <p style="font-size:14px;">Even more text that should appear on yet another line.</p>
    
#     <pre style="background-color: #e8e8e8; padding: 10px;">
#     <code>
#     def example_function():
#         return "This is a code block"
#     </code>
#     </pre>
    
#     <p style="font-size:14px;"><b>Bold Text</b></p>
#     <p style="font-size:14px;"><i>Italic Text</i></p>
    
#     <blockquote style="font-size:14px; color:gray;">
#         Blockquote text that should be properly formatted in markdown.
#     </blockquote>
    
#     <p style="font-size:14px;">Links: <a href="https://www.openai.com" style="color:orange;">OpenAI</a></p>
#     </div> """]

compétences=[texte_essai]+\
    [""" <div style="border:2px solid black; padding: 10px; background-color: #f0f0f0;">
    <h5 style="color:white;border:2px solid black; padding: 10px; background-color: #0175f2;"> suite ...</h5></div> """]*6


def show_text(slider_id,x,y):
    hover_text.set_content(compétences[slider_id])
    hover_text.style(f'position: absolute; left: {x}px; top: {y}px; visibility: visible;')

# Function to hide text on mouseout
def hide_text():
    hover_text.style('visibility: hidden;')

posX,posY=700,10

# Create the table with 7 rows and 2 columns
with ui.column(): 
    for i in range(7):
        with ui.row().classes('w-full no-wrap'):
            ui.label(questions[i]).classes('w-1/3')  
            slider = ui.slider(min=0, max=4, step=0.1).classes('w-2/3')
            slider.on('mouseover', lambda e, i=i: show_text(i,posX,posY))
            #slider.on('mouseout', lambda e: hide_text()) 
            slider.on('mousemove', lambda e, i=i: show_text(i,posX,posY))  # Show text when slider is moved
            slider.on('mousedown', lambda e, i= i:show_text(i,posX,posY))
            slider.on('click', lambda e,i= i:show_text(i,posX,posY))
            sliders.append(slider)

#Zone de texte
#ui.textarea(label='Text', placeholder='start typing')


# Add the "Enregistrer" button
ui.button('Enregistrer', on_click=save_positions)



ui.run()