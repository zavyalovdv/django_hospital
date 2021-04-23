import pytest
import unittest

from hospital import settings


class SettingsTest(unittest.TestCase):    
    def test_settings_is_configured(self):
        assert 'patient.apps.PatientConfig' in settings.INSTALLED_APPS
