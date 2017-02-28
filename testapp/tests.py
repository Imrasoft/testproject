from django.test import TestCase
from testapp.models import Group


class GroupTest(TestCase):
    def group_add_test(self):
        group_count = Group.objects.count()
        added_groups = Group.add_groups()
        self.assertEquals(Group.objects.count(), group_count + added_groups)

    def test_group_exists(self):
        class Grp(object):
            def __init__(self, name=None, uuid=None, query=None, count=None):
                self.name = name
                self.uuid = uuid
                self.query = query
                self.count = count

        rapidpro_mock_group = Grp(name='Test Group', uuid='random number', query=None, count=4)
        self.assertEquals(Group.group_exists(rapidpro_mock_group), False)
        Group.objects.create(name='Test Group', uuid='random number', query=None, count=4)
        self.assertEquals(Group.group_exists(rapidpro_mock_group), True)


'''
Created a class to hold the testing methods, group_add and group_exists.

To test adding groups

I find the number of groups in the local db.
I add new groups into the db and then use aasertequals to check if the two sets of variables
 (Group.objects.count() and (group_count + added_groups)are equal.
 If they are equal, the test will pass else it will fail.


To test if group exists

We define a replica of the group model and call it Grp. We then create the replica by assigning it a variable
mock group. We use assertEquals to equate  Group_exists method (which is defined in models.py) and "False".
If they are equal then test passes. and fails if vice verser.

We now use objects.creste to insert the group into the DB and again use assertEquals to check
if True and group_exists are the same.


'''