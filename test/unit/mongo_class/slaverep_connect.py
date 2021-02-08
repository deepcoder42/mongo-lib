#!/usr/bin/python
# Classification (U)

"""Program:  slaverep_connect.py

    Description:  Unit testing of SlaveRep.connect in mongo_class.py.

    Usage:
        test/unit/mongo_class/slaverep_connect.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import mongo_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_primary_attr2 -> Test primary attribute.
        test_primary_attr -> Test primary attribute.
        test_repset_attr2 -> Test repset attribute.
        test_repset_attr -> Test repset attribute.
        test_issecondary_attr2 -> Test issecondary attribute.
        test_issecondary_attr -> Test issecondary attribute.
        test_ismaster_attr2 -> Test ismaster attribute.
        test_ismaster_attr -> Test ismaster attribute.
        test_no_conn_list1 -> Test with no connections passed.
        test_no_conn_list -> Test with no connections passed.
        test_fail_connection2 -> Test with failed connection.
        test_fail_connection -> Test with failed connection.
        test_no_data2 -> Test with no data returned.
        test_no_data -> Test with no data returned.
        test_default2 -> Test with minimum number of arguments.
        test_default -> Test with minimum number of arguments.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "Mongo_Server"
        self.user = "mongo_user"
        self.japd = "mongo_pd"
        self.host = "host_server"
        self.port = 27017
        self.dbs = "test"
        self.coll = None
        self.db_auth = None
        self.repset = "mongo_repset"
        self.data = {"secondary": True, "ismaster": False,
                     "issecondary": True, "setName": "mongo_repset",
                     "primary": "primary_host"}
        self.msg = "Error:  This is not a Slave Replication server."

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_primary_attr2(self, mock_fetch):

        """Function:  test_primary_attr2

        Description:  Test primary attribute.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.SlaveRep(self.name, self.user, self.japd,
                                     self.host, self.port)
        mongo.connect()

        self.assertEqual(mongo.primary, "primary_host")

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_primary_attr(self, mock_fetch):

        """Function:  test_primary_attr

        Description:  Test primary attribute.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.SlaveRep(self.name, self.user, self.japd,
                                     self.host, self.port)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_repset_attr2(self, mock_fetch):

        """Function:  test_repset_attr2

        Description:  Test repset attribute.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.SlaveRep(self.name, self.user, self.japd,
                                     self.host, self.port)
        mongo.connect()

        self.assertEqual(mongo.repset, "mongo_repset")

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_repset_attr(self, mock_fetch):

        """Function:  test_repset_attr

        Description:  Test repset attribute.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.SlaveRep(self.name, self.user, self.japd,
                                     self.host, self.port)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_issecondary_attr2(self, mock_fetch):

        """Function:  test_issecondary_attr2

        Description:  Test issecondary attribute.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.SlaveRep(self.name, self.user, self.japd,
                                     self.host, self.port)
        mongo.connect()

        self.assertTrue(mongo.issecondary)

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_issecondary_attr(self, mock_fetch):

        """Function:  test_issecondary_attr

        Description:  Test issecondary attribute.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.SlaveRep(self.name, self.user, self.japd,
                                     self.host, self.port)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_ismaster_attr2(self, mock_fetch):

        """Function:  test_ismaster_attr2

        Description:  Test ismaster attribute.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.SlaveRep(self.name, self.user, self.japd,
                                     self.host, self.port)
        mongo.connect()

        self.assertFalse(mongo.ismaster)

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_ismaster_attr(self, mock_fetch):

        """Function:  test_ismaster_attr

        Description:  Test ismaster attribute.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.SlaveRep(self.name, self.user, self.japd,
                                     self.host, self.port)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_no_conn_list1(self, mock_fetch):

        """Function:  test_no_conn_list1

        Description:  Test with no connections passed.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.SlaveRep(self.name, self.user, self.japd,
                                     self.host, self.port)
        mongo.conn = True
        mongo.connect()

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.ismaster, mongo.issecondary),
            (self.name, self.user, self.japd, self.host, self.port, False,
             True))

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_no_conn_list(self, mock_fetch):

        """Function:  test_no_conn_list

        Description:  Test with no connections passed.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.SlaveRep(self.name, self.user, self.japd,
                                     self.host, self.port)
        mongo.conn = True

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(False, "Error Message")))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_fail_connection2(self, mock_fetch):

        """Function:  test_fail_connection2

        Description:  Test with failed connection.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.SlaveRep(self.name, self.user, self.japd,
                                     self.host, self.port)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.ismaster, mongo.issecondary),
            (self.name, self.user, self.japd, self.host, self.port, None,
             None))

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(False, "Error Message")))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_fail_connection(self, mock_fetch):

        """Function:  test_fail_connection

        Description:  Test with failed connection.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.SlaveRep(self.name, self.user, self.japd,
                                     self.host, self.port)

        self.assertEqual(mongo.connect(), (False, "Error Message"))

    @mock.patch("mongo_class.Server.disconnect", mock.Mock(return_value=True))
    @mock.patch("mongo_class.fetch_ismaster", mock.Mock(return_value={}))
    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    def test_no_data2(self):

        """Function:  test_no_data2

        Description:  Test with no data returned.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(self.name, self.user, self.japd,
                                     self.host, self.port)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.ismaster, mongo.issecondary),
            (self.name, self.user, self.japd, self.host, self.port, None,
             None))

    @mock.patch("mongo_class.Server.disconnect", mock.Mock(return_value=True))
    @mock.patch("mongo_class.fetch_ismaster", mock.Mock(return_value={}))
    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    def test_no_data(self):

        """Function:  test_no_data

        Description:  Test with no data returned.

        Arguments:

        """

        mongo = mongo_class.SlaveRep(self.name, self.user, self.japd,
                                     self.host, self.port)

        self.assertEqual(mongo.connect(), (False, self.msg))

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_default2(self, mock_fetch):

        """Function:  test_default2

        Description:  Test connect method with default arguments.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.SlaveRep(self.name, self.user, self.japd,
                                     self.host, self.port)
        mongo.connect()

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.ismaster, mongo.issecondary),
            (self.name, self.user, self.japd, self.host, self.port, False,
             True))

    @mock.patch("mongo_class.Server.connect",
                mock.Mock(return_value=(True, None)))
    @mock.patch("mongo_class.fetch_ismaster")
    def test_default(self, mock_fetch):

        """Function:  test_default

        Description:  Test connect method with default arguments.

        Arguments:

        """

        mock_fetch.return_value = self.data
        mongo = mongo_class.SlaveRep(self.name, self.user, self.japd,
                                     self.host, self.port)

        self.assertEqual(mongo.connect(), (True, None))


if __name__ == "__main__":
    unittest.main()