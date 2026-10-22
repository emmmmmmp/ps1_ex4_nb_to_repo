from sklearn.ensemble import RandomForestClassifier

def features_and_target(df, predictors, target):
    return df[predictors], df[target].values


def train_and_predict(train_X, train_y, valid_X, **model_parameters):
    classifier = RandomForestClassifier(**model_parameters)
    classifier.fit(train_X, train_y)
    return classifier, classifier.predict(train_X), classifier.predict(valid_X)