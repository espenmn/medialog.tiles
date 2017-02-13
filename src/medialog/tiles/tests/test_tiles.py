# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from medialog.tiles.interfaces import ITiles
from medialog.tiles.testing import MEDIALOG_TILES_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class TilesIntegrationTest(unittest.TestCase):

    layer = MEDIALOG_TILES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Tiles')
        schema = fti.lookupSchema()
        self.assertEqual(ITiles, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Tiles')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Tiles')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(ITiles.providedBy(obj))

    def test_adding(self):
        obj = api.content.create(
            container=self.portal,
            type='Tiles',
            id='Tiles',
        )
        self.assertTrue(ITiles.providedBy(obj))
