#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(reticulate)
reticulate::use_python("C:/Users/licor/AppData/Local/Continuum/anaconda3/python.exe", required = TRUE)
#Sys.which("python")
source_python("C:/Users/licor/OneDrive/Desktop/qmss/spring/practinum/summarizer.py")


ui <- fluidPage(
    fluidPage(
        titlePanel("Summarizer"),
        sidebarPanel(sliderInput(inputId = "num", 
                    label = "Compress original text to", 
                    value = 0.3, min = 0, max = 1),
        textAreaInput(inputId = "complaint", label = "Enter the original text", value = "", 
                      width = "300px", height = "400px", placeholder = NULL)),
        mainPanel(h3("Summarized Text"),
                  textOutput("summary")
                  )
    ))



server <- function(input, output) {

    output$summary <- renderPrint({
        summarizer(input$complaint, input$num)
    })
}


shinyApp(ui = ui, server = server)
