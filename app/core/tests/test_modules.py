from django.test import TestCase
from django.contrib.auth import get_user_model


class ModuleTest( TestCase ):

    def test_create_user_with_email_successfull(self):
        """Create a successful user with email"""
        email = "sangam.angre@gmail.com"
        password = "test!23"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual( user.email, email )
        self.assertTrue( user.check_password( password ) )

    def test_create_user_with_nomalized_email(self):
        email = "sangam.angre@GMAIL.com"
        password = "test!23"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual( user.email, email.lower() )

    def test_invalid_email_raise(self):
        email = ""
        password = "test!23"

        with self.assertRaises( ValueError ):
            get_user_model().objects.create_user(
                email=email,
                password=password
            )

    def test_create_super_user_with_email_successfull(self):
        """Create a successful user with email"""
        email = "sangam.angre123@gmail.com"
        password = "test!23"
        user = get_user_model().objects.create_super_user(
            email=email,
            password=password
        )

        self.assertTrue( user.is_active )
        self.assertTrue( user.is_staff )
