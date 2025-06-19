import urllib.parse
import codecs

# Encoded string
xmlname = '%73%6D%77%62%76%61%67%63%61%2E%70%6C%70%6E%79%7A%75%62%2E%66%76%67%72'

# Step 1: URL decode
decoded_url = urllib.parse.unquote(xmlname)

# Step 2: Apply ROT13
final_result = codecs.decode(decoded_url, 'rot_13')

# Output the result
print("Decoded string:", final_result)
