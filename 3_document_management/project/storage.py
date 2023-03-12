from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = self.__find_by_id(category_id, self.categories)
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.__find_by_id(topic_id, self.topics)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.__find_by_id(document_id, self.documents)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = self.__find_by_id(category_id, self.categories)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.__find_by_id(topic_id, self.topics)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.__find_by_id(document_id, self.documents)
        self.documents.remove(document)

    def get_document(self, document_id):
        document = self.__find_by_id(document_id, self.documents)
        return document

    def __find_by_id(self, id, list_of_objcts):
        for obj in list_of_objcts:
            if obj.id == id:
                return obj
    def __repr__(self):
        return  '\n'.join(repr(x) for x in self.documents)
