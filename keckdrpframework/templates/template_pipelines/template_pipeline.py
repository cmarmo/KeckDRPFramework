"""
This is a template pipeline.

"""

from pipelines.base_pipeline import BasePipeline


class TemplatePipeline(BasePipeline):
    """
    The template pipeline.
    """

    event_table = {"next_file": ("simple_fits_reader", "file_ready", "file_ready"), "file_ready": ("template_action", None, None)}

    def __init__(self, context):
        """
        Constructor
        """
        BasePipeline.__init__(self, context)

    def template_action(self, action, context):
        print("Template action", action)
        return None
