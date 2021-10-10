import json

class Get_Data:
    def personal_data(self):
        try:
            with open('student.json', 'r') as f:
                # Getting data from the student file and returning it
                data = json.load(f)
                return data                
        except Exception as e:    
            return -1

    def subject_data(self):
        try:
            with open('subject.json', 'r') as f:
                # Getting data from the subject file and returning it
                data = json.load(f)
                return data                
        except Exception as e:    
            return -1

    def marks_data(self):
        try:
            with open('marks.json', 'r') as f:
                # Getting data from the marks file and returning it
                data = json.load(f)
                return data               
        except Exception as e:    
            return -1

class Write_Data:
    def personal_data(self, dict):
        with open('student.json', 'w') as f:
            # Writing Json data to the student file
            json.dump(dict, f, indent=3) 

    def subject_data(self, dict):
        with open('subject.json', 'w') as f:
            # Writing Json data to the subject file
            json.dump(dict, f, indent=3) 

    def marks_data(self, dict):
        with open('marks.json', 'w') as f:
            # Writing Json data to the marks file
            json.dump(dict, f, indent=3) 

class Search_Data:
    def searchAndWrite(self, filename, rollno):
        get_data = Get_Data()
        if filename != -1:
            data_dict = filename
            if rollno in data_dict:
                with open('f.json', 'w') as f:
                    json.dump(data_dict[rollno], f, indent=3)
                    
                return 1
            else:
                return -1
        else:
            return -1
