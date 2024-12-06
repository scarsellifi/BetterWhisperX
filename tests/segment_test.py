import pytest
from faster_whisper import utils
import whisperx


def test_transcription_and_alignment():
    device = "cpu"  # cuda
    audio_file = "tests/testwhisper.wav"
    batch_size = 16  # reduce if low on GPU mem
    compute_type = "int8"  # change to "int8" if low on GPU mem (may reduce accuracy)

    # Load model
    model = whisperx.load_model(
        "large-v3-turbo", device=device, compute_type=compute_type
    )
    audio = whisperx.load_audio(audio_file)

    # Transcription
    result = model.transcribe(audio, batch_size=batch_size)
    assert "segments" in result
    assert len(result["segments"]) > 0
    print(result["segments"])  # before alignment

    # Alignment
    model_a, metadata = whisperx.load_align_model(
        language_code=result["language"], device=device
    )
    aligned_result = whisperx.align(
        result["segments"],
        model_a,
        metadata,
        audio,
        device,
        return_char_alignments=False,
    )

    assert "segments" in aligned_result
    assert len(aligned_result["segments"]) > 0
    print(aligned_result["segments"])  # after alignment

    # Cleanup
    del model, model_a
