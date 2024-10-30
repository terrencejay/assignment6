#Write a program that will search through product reviews list and look for keywords like "good" and "bad"
#capitalize each keyword then print out the review with the keyword capitalized.

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

def product_review():
    #Create a variable named 'review' using it to replace the key word with the capitalized version. '.replace' searches for the instance of the word in the sentence and replaces it with the second value in the ()
    excellent_product = [review.replace("excellent","EXCELLENT") for review in reviews if "excellent" in review.lower()]
    good_product = [review.replace("good","GOOD") for review in reviews if "good" in review.lower()]
    average_product = [review.replace("average","AVERAGE") for review in reviews if "average" in review.lower()]
    bad_product = [review.replace("bad","BAD") for review in reviews if "bad" in review.lower()]
    poor_product = [review.replace("poor","POOR").replace("Poor","POOR") for review in reviews if "poor" in review.lower()]
    print(excellent_product, good_product,average_product,bad_product,poor_product)

def tallies():
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    counts = {word: 0 for word in positive_words}

    for review in reviews:
        rev = review.lower()
        for word in positive_words:
            counts[word] += rev.count(word)
    print(counts)

    neg_counts = {word: 0 for word in negative_words}
    
    for review in reviews:
        neg = review.lower()
        for word in negative_words:
            neg_counts[word] += neg.count(word)
    print(neg_counts)



    

product_review()
tallies()
summary = ""

for review in reviews:
    summary += review[:30] + "\n"

print (summary)
