#arbre de décision

# setwd("C:/Users/INTEL/Desktop/....")

#Charger la bibliothèque « rpart » et « rpart.plot »
library(rpart.plot)
library(rpart)

titanic<-read.csv2(file = file.choose(),header=T,sep=';') 
titanic
summary(Titanic)
str(titanic)

titanic = na.omit(titanic) 
titanic

titanic$Survived = factor(titanic$Survived, levels = c(0, 1), labels = c("No", "Yes"))


#Changer les valeurs Pclass (1, 2, 3) par (Upper , Middle, Lower) respectivement
titanic$Pclass = factor(titanic$Pclass, levels = c(1, 2, 3), labels = c("Upper", "Middle", "Lower"))

titanic

str(titanic)
summary(titanic)
nrow(titanic)
dim(titanic)

#generer 5 nombres dans l'intarvalle [0,10]
#sample(10,5)

#Titanic_training : contenant un échantillon de 100 individus à partir de titanic. 
indice = sample(nrow(titanic), 100)

titanic_training = titanic[indice, ]
titanic_training
nrow(titanic_training)
#Titanic_test : contenant le reste de Titanic. 
titanic_test = titanic[-indice, ]
titanic_test
nrow(titanic_test)
dim(titanic_test)

prop.table(table(titanic_training$Survived))

ar = rpart(Survived~., data = titanic_training, method = "class")
ar

# la représentation graphique de l'arbre en utilisant rpart.plot().
rpart.plot(ar)


pred = predict(ar, titanic_test, type = "class")
pred
titanic_test

table_mat = table(titanic_test$Survived, pred)
table_mat  

accuracy = sum(diag(table_mat))/sum(table_mat)
accuracy
