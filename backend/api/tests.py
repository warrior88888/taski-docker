from http import HTTPStatus

from django.test import Client, TestCase

from .models import Task


class TaskiAPITestCase(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_list_exists(self):
        """Проверка доступности списка задач."""
        response = self.guest_client.get("/api/tasks/")
        self.assertEqual(  # noqa: PT009
            response.status_code,  # type: ignore[reportAttributeAccessIssue]
            HTTPStatus.OK,
        )

    def test_task_creation(self):
        """Проверка создания задачи."""
        data = {"title": "Test", "description": "Test"}
        response = self.guest_client.post("/api/tasks/", data=data)
        self.assertEqual(  # noqa: PT009
            response.status_code,  # type: ignore[reportAttributeAccessIssue]
            HTTPStatus.CREATED,
        )
        self.assertTrue(Task.objects.filter(title="Test").exists())  # noqa: PT009
