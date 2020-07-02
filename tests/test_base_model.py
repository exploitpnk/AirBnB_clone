#!/usr/bin/python3
""" Unittest for BaseModel Class """

from models.base_model import BaseModel
import unittest
from unittest.mock import patch
from time import sleep
import datetime

class Test_init(unittest.TestCase):
    """ Test for unittest """
    def setUp(self):
        """ setting for the methods """
        pass

    def tearDown(self):
        """ teardown for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_instance_creation_no_arg(self):
        """ without arguments """
        t1 = BaseModel()
        self.assertTrue(hasattr(t1, "id"))
        self.assertTrue(hasattr(t1, "created_at"))
        self.assertTrue(hasattr(t1, "updated_at"))

    def test_attr_types(self):
        """ without arguments """
        t1 = BaseModel()
        self.assertEqual(type(t1.id), str)
        self.assertEqual(type(t1.created_at), datetime.datetime)
        self.assertEqual(type(t1.updated_at), datetime.datetime)

    def test_id(self):
        """ Check uuid generated """
        t1 = BaseModel()
        t2 = BaseModel()
        t3 = BaseModel()
        t4 = BaseModel()
        self.assertFalse(t1.id == t2.id)
        self.assertFalse(t1.id == t3.id)
        self.assertFalse(t1.id == t4.id)
        self.assertFalse(t2.id == t3.id)
        self.assertFalse(t2.id == t4.id)
        self.assertFalse(t3.id == t4.id)

    def test_arg(self):
        """ Test *args """
        t1 = BaseModel(1)
        t2 = BaseModel(1, "t2")
        t3 = BaseModel(1, "t3", (1, 2))
        t4 = BaseModel(1, "t4", (1, 2), [1, 2])

    def test_arg_def(self):
        """ default arguments """
        t1 = BaseModel(1, "test", (1, 2), [1, 2])
        self.assertTrue(hasattr(t1, "id"))
        self.assertTrue(hasattr(t1, "created_at"))
        self.assertTrue(hasattr(t1, "updated_at"))

    def test_kwarg(self):
        """ Argument is kwarg """
        arg = {'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
               'created_at': '2017-09-28T21:05:54.119427',
               '__class__': 'BaseModel',
               'updated_at': '2017-09-28T21:05:54.119572'}

        t1 = BaseModel(**arg)
        self.assertTrue(hasattr(t1, "id"))
        self.assertTrue(hasattr(t1, "created_at"))
        self.assertTrue(hasattr(t1, "updated_at"))
        self.assertTrue(hasattr(t1, "__class__"))
        self.assertTrue(t1.__class__ not in t1.__dict__)

        self.assertEqual(t1.id, 'b6a6e15c-c67d-4312-9a75-9d084935e579')
        self.assertEqual(t1.created_at.isoformat(),
                         '2017-09-28T21:05:54.119427')
        self.assertEqual(t1.updated_at.isoformat(),
                         '2017-09-28T21:05:54.119572')

    def test_N_arg(self):
        """ new atributes """
        n = {"name": "Luis"}
        t1 = BaseModel(**n)
        self.assertTrue(hasattr(t1, "id"))
        self.assertTrue(hasattr(t1, "created_at"))
        self.assertTrue(hasattr(t1, "updated_at"))
        self.assertEqual(t1.name, "Luis")

    def test_time(self):
        """ test time formarts """
        arg = {'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
               'created_at': '2017-09-28T21:05:54.119427',
               '__class__': 'BaseModel',
               'updated_at': '2017-09-28T21:05:54.119572'}
        t1 = BaseModel(**arg)
        self.assertEqual(t1.created_at.isoformat(),
                         '2017-09-28T21:05:54.119427')
        self.assertEqual(t1.updated_at.isoformat(),
                         '2017-09-28T21:05:54.119572')
        self.assertEqual(type(t1.created_at), datetime.datetime)
        self.assertEqual(type(t1.updated_at), datetime.datetime)
