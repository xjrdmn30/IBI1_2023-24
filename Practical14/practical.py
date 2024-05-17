import xml.dom.minidom
import xml.sax
from xml.sax.xmlreader import AttributesImpl
import matplotlib.pyplot as plt
from datetime import datetime
# Measure start time for DOM parsing
time1 = datetime.now()
# Parse the XML file using DOM
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName('term')
# Count the number of terms for each ontology using DOM
molecular_function_count1 = 0
biological_process_count1 = 0
cellular_component_count1 = 0

for term in terms:
    namespace = term.getElementsByTagName('namespace')[0].firstChild.nodeValue
    if namespace == "molecular_function":
        molecular_function_count1 += 1
    elif namespace == "biological_process":
        biological_process_count1 += 1
    elif namespace == "cellular_component":
        cellular_component_count1 += 1

# Measure end time for DOM parsing
time2 = datetime.now()

# Store DOM counts in a list
dom = [molecular_function_count1, biological_process_count1, cellular_component_count1]

# Print DOM results and time taken
print("DOM API \n", "molecular_function: ", molecular_function_count1, '\n', "biological_process: ", biological_process_count1, '\n', "cellular_component: ", cellular_component_count1)
print("DOM API time: ", time2 - time1)


# Define SAX ContentHandler to handle XML parsing events
class TermHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.namespace = ""
        self.molecular_function_count2 = 0
        self.biological_process_count2 = 0
        self.cellular_component_count2 = 0

    def startElement(self, name, attrs):
        if name == "namespace":
            self.namespace = ""

    def characters(self, content):
        self.namespace = content

    def endElement(self, name):
        if name == "namespace":
            if self.namespace == "molecular_function":
                self.molecular_function_count2 += 1
            elif self.namespace == "biological_process":
                self.biological_process_count2 += 1
            elif self.namespace == "cellular_component":
                self.cellular_component_count2 += 1


# Measure start time for SAX parsing
time3 = datetime.now()
# Create SAX parser and parse the XML file
handler = TermHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse("go_obo.xml")
# Measure end time for SAX parsing
time4 = datetime.now()
# Store SAX counts in a list
sax = [handler.molecular_function_count2, handler.biological_process_count2, handler.cellular_component_count2]
# Print SAX results and time taken
print("SAX API \n", "molecular_function: ", handler.molecular_function_count2, '\n', "biological_process: ",
      handler.biological_process_count2, '\n', "cellular_component: ", handler.cellular_component_count2)
print("SAX API time: ", time4 - time3)
# Compare time taken by DOM and SAX
if time4 - time3 > time2 - time1:
    print("DOM is quicker")
else:
    print("SAX is quicker")
# Plot DOM results
plt.bar(ontologies, dom, label="DOM")
plt.xlabel("ontology")
plt.ylabel("number of terms")
plt.title("DOM API")
plt.legend()
plt.show()
plt.clf()
# Plot SAX results
plt.bar(ontologies, sax, label="SAX")
plt.xlabel("ontology")
plt.ylabel("number of terms")
plt.title("SAX API")
plt.legend()
plt.show()
plt.clf()
