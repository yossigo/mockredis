from nose.tools import eq_, ok_

from mockredis.tests.fixtures import setup, teardown


class TestRedisConfig(object):
    """Redis config set/get tests"""

    def setup(self):
        setup(self)

    def teardown(self):
        teardown(self)

    def test_config_set(self):
        ok_(self.redis.config_set('loglevel', 'debug'))
        eq_(self.redis.config_get('loglevel'), {'loglevel': 'debug'})
        ok_(self.redis.config_set('loglevel', 'notice'))
        eq_(self.redis.config_get('loglevel'), {'loglevel': 'notice'})
        eq_(self.redis.config_get('loglev*'), {'loglevel': 'notice'})

    def test_config_set_int_value(self):
        ok_(self.redis.config_set('hz', 12))
        eq_(self.redis.config_get('hz'), {'hz': '12'})
        ok_(self.redis.config_set('hz', 10))
        eq_(self.redis.config_get('hz'), {'hz': '10'})

