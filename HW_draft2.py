import re
def get_hashtag_ranking(input_text):
    hashtag_list=re.findall("#", input_text)
    hashtag_count={}
    for hashtag in hashtag_list:
        if hashtag in hashtag_count:
            hashtag_count[hashtag]+=1
        else:
            hashtag_count[hashtag]=1
    def get_frequency(hashtag_count_pair):
        return hashtag_count_pair[1]
    sorted_hashtags=sorted(hashtag_count.items(),key=get_frequency, reverse=True)
    output_list=[hashtag for (hashtag,count) in sorted_hashtags]
    return output_list


fout2= open("hastag_examples.txt", "r")
for line in fout2:
    a= get_hashtag_ranking("hastag_examples.txt")
    print(a)
