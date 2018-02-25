# If you don't have them, install the required packages
# install.packages("e1071")
# install.packages("RTextTools")

library(e1071)
library(RTextTools)

# Load the data from the csv file
data <- read.csv(paste("./datasets/dmoz0409_Arts_finaltest.csv",sep=""), header = TRUE)

# Create the document term matrix
dtMatrix <- create_matrix(data["text4"])

# Configure the training data
container <- create_container(dtMatrix, data$istrue, trainSize=1:34868, virgin=FALSE)

# train a SVM Model
model <- train_model(container, "SVM", kernel="linear", cost=1)

# new data
predictionData <- list("http holloway co nz", "http wwww facebook com", "http www newadvent org")

# create a prediction document term matrix
# trace("create_matrix", edit=T)
predMatrix <- create_matrix(predictionData, originalMatrix=dtMatrix)

# create the corresponding container
predSize = length(predictionData);
predictionContainer <- create_container(predMatrix, labels=rep(0,predSize), testSize=1:predSize, virgin=FALSE)

# predict
results <- classify_model(predictionContainer, model)
results
