# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from medialog.tiles.testing import MEDIALOG_TILES_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that medialog.tiles is properly installed."""

    layer = MEDIALOG_TILES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if medialog.tiles is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'medialog.tiles'))

    def test_browserlayer(self):
        """Test that IMedialogTilesLayer is registered."""
        from medialog.tiles.interfaces import (
            IMedialogTilesLayer)
        from plone.browserlayer import utils
        self.assertIn(IMedialogTilesLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = MEDIALOG_TILES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['medialog.tiles'])

    def test_product_uninstalled(self):
        """Test if medialog.tiles is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'medialog.tiles'))

    def test_browserlayer_removed(self):
        """Test that IMedialogTilesLayer is removed."""
        from medialog.tiles.interfaces import \
            IMedialogTilesLayer
        from plone.browserlayer import utils
        self.assertNotIn(IMedialogTilesLayer, utils.registered_layers())
