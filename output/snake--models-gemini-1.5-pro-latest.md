The `response.text` quick accessor only works when the response contains a valid `Part`, but none was returned. Check the `candidate.safety_ratings` to see if the response was blocked.

response:
GenerateContentResponse(
    done=True,
    iterator=None,
    result=glm.GenerateContentResponse({
      "candidates": [
        {
          "finish_reason": 4,
          "index": 0,
          "safety_ratings": [],
          "token_count": 0,
          "grounding_attributions": []
        }
      ]
    }),
)
