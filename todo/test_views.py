from django.test import TestCase
from .models import Item

# Create your tests here.

class TestViews(TestCase):

    # . indicates pass
    # def test_this_thing_works(self):
    #     self.assertEqual(1, 1)

    # F indicates fail
    # def test_this_thing_works2(self):
    #     self.assertEqual(1, 3)

    # # E indicates error
    # def test_this_thing_works3(self):
    #     self.assertEqual(1, )


    # def test_this_thing_works4(self):
    #     self.assertEqual(1, 4)


    def test_get_todo_list(self):
        # get slash to get the homepage
        response = self.client.get('/')
        # check that the request is successful
        self.assertEqual(response.status_code, 200)
        # which template should be used in the response
        self.assertTemplateUsed(response, 'todo/todo_list.html')


    def test_get_add_item_page(self):
        # get slash to get the homepage
        response = self.client.get('/add')
        # check that the request is successful
        self.assertEqual(response.status_code, 200)
        # which template should be used in the response
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        item = Item.objects.create(name = 'Test Todo Item')
        # get slash to get the homepage
        response = self.client.get(f'/edit/{item.id}')
        # check that the request is successful
        self.assertEqual(response.status_code, 200)
        # which template should be used in the response
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    
    def test_can_add_item(self):
        response = self.client.post('/add', {'name': 'Test Added Item'})
        # Does the user get redirected to updated list after action?
        self.assertRedirects(response, '/')


    def test_can_delete_item(self):
        item = Item.objects.create(name = 'Test Todo Item')
        # get slash to get the homepage
        response = self.client.get(f'/delete/{item.id}')
        # Does the user get redirected to updated list after action?
        self.assertRedirects(response, '/')
        # Check if the item exists after deleting
        existing_items = Item.objects.filter(id=item.id)
        # No item with this id should exist now
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        item = Item.objects.create(name = 'Test Todo Item', done=True)
        # get slash to get the homepage
        response = self.client.get(f'/toggle/{item.id}')
        # Does the user get redirected to updated list after action?
        self.assertRedirects(response, '/')
        # Check item id has been updated
        updated_item = Item.objects.get(id=item.id)
        # The item should not marked as done now
        self.assertFalse(updated_item.done)


    def test_can_edit_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.post(f'/edit/{item.id}', {'name': 'Updated Name'})
        # Does the user get redirected to updated list after action?
        self.assertRedirects(response, '/')
        # Check item id has been updated
        updated_item = Item.objects.get(id=item.id)
        # Check item name is updated correctly
        self.assertEqual(updated_item.name, 'Updated Name')