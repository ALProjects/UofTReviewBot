import praw
import os
import ReviewBotSpreadsheet


reddit = praw.Reddit('reviewBot')
print(reddit.auth.scopes())

subreddit = reddit.subreddit("test")

def get_restaurant(restaurant_name):
    return ReviewBotSpreadsheet.find_restaurant(restaurant_name)

def main():

    used_review_list = []

    if not os.path.isfile("posts_replied_to.txt"):
        posts_replied_to =[]



    else:
        with open ("posts_replied_to.txt", "r") as f:
            posts_replied_to = f.read()
            posts_replied_to = posts_replied_to.split("\n")
            posts_replied_to = list(filter(None, posts_replied_to))


    list_of_valid_restaurants = ReviewBotSpreadsheet.list_restaurants()



    for submission in subreddit.hot(limit=10):
        print('Submission id is: ')
        print(submission.id)

        if submission.id != '6bkzra': #This is to ignore the pinned post
            #for top_level_comments in submission.comments:
            """
            print('Comment id is:')
            print(comments.id)
            print('Comment is:' )
            print(comments.body)
            """
            submission.comments.replace_more(limit=0)
            for comments in submission.comments.list():

                if comments.id not in posts_replied_to and comments.author != "UofTFoodReviewBot":
                    comment = str(comments.body)
                    #print("comment thingy: ")
                    for restaurant in list_of_valid_restaurants:
                        print("parsing through list of restaurants")
                        my_restaurant = restaurant.lower()
                        my_comment = comment.lower()
                        if my_restaurant in my_comment and restaurant != "":
                            if len(used_review_list) != 0:
                                for used_review in used_review_list: #code doesn't run to here, why? There is no used_review_list...
                                    print("parsing used review list")
                                    if used_review != get_restaurant(restaurant):
                                        print("review not in used review list")
                                        this_restaurant_review = get_restaurant(restaurant)
                                        #used_review += this_restaurant_review
                                        used_review_list.append(this_restaurant_review)
                                        comments.reply(this_restaurant_review)
                                        posts_replied_to.append(comments.id)

                            else:
                                used_review_list.append(get_restaurant(restaurant))
                                comments.reply(get_restaurant(restaurant))
                                posts_replied_to.append(comments.id)


    with open("posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")





if __name__ == '__main__':
    main()






