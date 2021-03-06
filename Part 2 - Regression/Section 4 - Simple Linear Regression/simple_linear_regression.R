#simple linear regression

# Importing the dataset
dataset = read.csv('Salary_Data.csv')
# dataset = dataset[, 2:3]

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(test_set[, 2:3])

#fitter linear regression to training set
regressor = lm(formula = Salary ~ YearsExperience,
               training_set)

#predicting test set results
y_pred = predict(regressor,newdata = test_set)

#visualising train set results
#install.packages('ggplot2')
library(ggplot2)
ggplot() + 
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             colour = 'red') +
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor,training_set)),
             colour = 'blue') +
  ggtitle('Salary vs Experience (training set)') + 
  xlab('year of experience') +
  ylab('saraly')

#visualising test set results
ggplot() + 
  geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary),
             colour = 'red') +
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor,training_set)),
            colour = 'blue') +
  ggtitle('Salary vs Experience (test set)') + 
  xlab('year of experience') +
  ylab('saraly')



