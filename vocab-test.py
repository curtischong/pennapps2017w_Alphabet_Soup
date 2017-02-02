import skipthoughts
model = skipthoughts.load_model()

vectors = skipthoughts.encode(model, X)
