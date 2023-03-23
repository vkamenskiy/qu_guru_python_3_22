import os
import allure
from dotenv import load_dotenv
from selene import have, be

load_dotenv()

LOGIN = os.getenv("DEMOSHOP_LOGIN")
WEB_URL = os.getenv("DEMOSHOP_WEB_URL")


def test_add_product_to_cart(app, demoshop):
    with allure.step('Open start page'):
        app.open("")

    with allure.step('Add product to cart'):
        demoshop.add_product_to_cart()

    with allure.step('Check product in cart'):
        app.element(".header-links #topcartlink").click()
        app.element(".product-name").should(have.text('Build your own cheap computer'))

    with allure.step('Remove products from the cart'):
        app.element('.remove-from-cart > [name = "removefromcart"]').click()
        app.element('.update-cart-button').click()
        app.element('div.order-summary-content').should(have.text('Your Shopping Cart is empty!'))


def test_delete_product_from_the_cart(app, demoshop):
    with allure.step('Open start page'):
        app.open("")

    with allure.step('Add product to cart'):
        demoshop.add_product_to_cart()

    with allure.step('Delete product from the cart'):
        app.element(".header-links #topcartlink").click()
        app.element('.remove-from-cart > [name = "removefromcart"]').click()
        app.element('.update-cart-button').click()
        app.element(".order-summary-content").should(have.text('Your Shopping Cart is empty!'))


def test_add_product_to_wishlist(app, demoshop):
    with allure.step('Open start page'):
        app.open("")

    with allure.step('Add product to wishlist'):
        demoshop.add_product_to_wishlist()

    with allure.step('Check product in wishlist'):
        app.element('.header-links .ico-wishlist').click()
        app.element('.cart-item-row .product > [href="/smartphone"]').should(have.text('Smartphone'))

    with allure.step('Remove products from the wishlist'):
        app.element('.remove-from-cart > [name = "removefromcart"]').click()
        app.element('.update-wishlist-button').click()
        app.element('.wishlist-content').should(have.text('The wishlist is empty!'))


def test_delete_product_from_the_wishlist(app, demoshop):
    with allure.step('Open start page'):
        app.open("")

    with allure.step('Add product to wishlist'):
        demoshop.add_product_to_wishlist()

    with allure.step('Delete product from the wishlist'):
        app.element('.header-links .ico-wishlist').click()
        app.element('.remove-from-cart > [name = "removefromcart"]').click()
        app.element('.update-wishlist-button').click()
        app.element('.wishlist-content').should(have.text('The wishlist is empty!'))


def test_logout(app):
    with allure.step('Open start page'):
        app.open("")

    with allure.step('Verify successful authorization'):
        app.element(".account").should(have.text(LOGIN))

    with allure.step('Logout'):
        app.element('.ico-logout').click()
        app.element('.ico-login').should(be.visible)

