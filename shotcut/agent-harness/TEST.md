# Test Results — Shotcut CLI Harness

## Test Results

Last run: 2026-03-06

```
tarunai_connect/shotcut/tests/test_core.py::TestTimecode::test_plain_frame_number PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTimecode::test_hh_mm_ss_mmm PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTimecode::test_hh_mm_ss PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTimecode::test_seconds_decimal PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTimecode::test_roundtrip PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTimecode::test_invalid_timecode PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTimecode::test_negative_frames PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTimecode::test_frames_to_seconds PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTimecode::test_seconds_to_frames PASSED
tarunai_connect/shotcut/tests/test_core.py::TestMltXml::test_create_blank_project PASSED
tarunai_connect/shotcut/tests/test_core.py::TestMltXml::test_write_and_parse PASSED
tarunai_connect/shotcut/tests/test_core.py::TestMltXml::test_properties PASSED
tarunai_connect/shotcut/tests/test_core.py::TestMltXml::test_mlt_to_string PASSED
tarunai_connect/shotcut/tests/test_core.py::TestSession::test_new_session PASSED
tarunai_connect/shotcut/tests/test_core.py::TestSession::test_new_project PASSED
tarunai_connect/shotcut/tests/test_core.py::TestSession::test_save_and_open PASSED
tarunai_connect/shotcut/tests/test_core.py::TestSession::test_undo_redo PASSED
tarunai_connect/shotcut/tests/test_core.py::TestSession::test_open_nonexistent PASSED
tarunai_connect/shotcut/tests/test_core.py::TestSession::test_save_without_project PASSED
tarunai_connect/shotcut/tests/test_core.py::TestSession::test_status PASSED
tarunai_connect/shotcut/tests/test_core.py::TestProject::test_new_project PASSED
tarunai_connect/shotcut/tests/test_core.py::TestProject::test_new_project_invalid_profile PASSED
tarunai_connect/shotcut/tests/test_core.py::TestProject::test_project_info PASSED
tarunai_connect/shotcut/tests/test_core.py::TestProject::test_list_profiles PASSED
tarunai_connect/shotcut/tests/test_core.py::TestProject::test_save_project PASSED
tarunai_connect/shotcut/tests/test_core.py::TestProject::test_open_and_info PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTimeline::test_list_tracks_initial PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTimeline::test_add_video_track PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTimeline::test_add_audio_track PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTimeline::test_add_invalid_track_type PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTimeline::test_remove_track PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTimeline::test_remove_background_track_fails PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTimeline::test_add_clip_file_not_found PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTimeline::test_add_and_list_clip PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTimeline::test_remove_clip PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTimeline::test_trim_clip PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTimeline::test_split_clip PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTimeline::test_move_clip PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTimeline::test_set_track_name PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTimeline::test_mute_unmute PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTimeline::test_show_timeline PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTimeline::test_add_blank PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTimeline::test_undo_add_track PASSED
tarunai_connect/shotcut/tests/test_core.py::TestFilters::test_list_available_filters PASSED
tarunai_connect/shotcut/tests/test_core.py::TestFilters::test_list_by_category PASSED
tarunai_connect/shotcut/tests/test_core.py::TestFilters::test_get_filter_info PASSED
tarunai_connect/shotcut/tests/test_core.py::TestFilters::test_get_unknown_filter PASSED
tarunai_connect/shotcut/tests/test_core.py::TestFilters::test_add_filter_to_clip PASSED
tarunai_connect/shotcut/tests/test_core.py::TestFilters::test_add_filter_to_track PASSED
tarunai_connect/shotcut/tests/test_core.py::TestFilters::test_add_global_filter PASSED
tarunai_connect/shotcut/tests/test_core.py::TestFilters::test_remove_filter PASSED
tarunai_connect/shotcut/tests/test_core.py::TestFilters::test_set_filter_param PASSED
tarunai_connect/shotcut/tests/test_core.py::TestFilters::test_undo_add_filter PASSED
tarunai_connect/shotcut/tests/test_core.py::TestMedia::test_probe_nonexistent PASSED
tarunai_connect/shotcut/tests/test_core.py::TestMedia::test_probe_basic PASSED
tarunai_connect/shotcut/tests/test_core.py::TestMedia::test_list_media_empty PASSED
tarunai_connect/shotcut/tests/test_core.py::TestMedia::test_list_media_with_clip PASSED
tarunai_connect/shotcut/tests/test_core.py::TestMedia::test_check_media_files PASSED
tarunai_connect/shotcut/tests/test_core.py::TestExport::test_list_presets PASSED
tarunai_connect/shotcut/tests/test_core.py::TestExport::test_get_preset_info PASSED
tarunai_connect/shotcut/tests/test_core.py::TestExport::test_unknown_preset PASSED
tarunai_connect/shotcut/tests/test_core.py::TestExport::test_render_no_project PASSED
tarunai_connect/shotcut/tests/test_core.py::TestExport::test_render_no_overwrite PASSED
tarunai_connect/shotcut/tests/test_core.py::TestIntegration::test_full_workflow PASSED
tarunai_connect/shotcut/tests/test_core.py::TestIntegration::test_save_load_roundtrip_preserves_filters PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTransitions::test_list_available_transitions PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTransitions::test_list_by_category_video PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTransitions::test_list_by_category_audio PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTransitions::test_get_transition_info PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTransitions::test_get_transition_info_invalid PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTransitions::test_add_transition PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTransitions::test_add_transition_with_params PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTransitions::test_add_wipe_transition PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTransitions::test_add_transition_invalid_track PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTransitions::test_add_raw_service_transition PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTransitions::test_list_transitions_empty PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTransitions::test_list_transitions_after_add PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTransitions::test_remove_transition PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTransitions::test_remove_transition_invalid_index PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTransitions::test_set_transition_param PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTransitions::test_undo_add_transition PASSED
tarunai_connect/shotcut/tests/test_core.py::TestTransitions::test_multiple_transitions PASSED
tarunai_connect/shotcut/tests/test_core.py::TestCompositing::test_list_blend_modes PASSED
tarunai_connect/shotcut/tests/test_core.py::TestCompositing::test_set_track_blend_mode PASSED
tarunai_connect/shotcut/tests/test_core.py::TestCompositing::test_set_blend_mode_invalid PASSED
tarunai_connect/shotcut/tests/test_core.py::TestCompositing::test_set_blend_mode_background_track PASSED
tarunai_connect/shotcut/tests/test_core.py::TestCompositing::test_get_track_blend_mode_default PASSED
tarunai_connect/shotcut/tests/test_core.py::TestCompositing::test_get_track_blend_mode_after_set PASSED
tarunai_connect/shotcut/tests/test_core.py::TestCompositing::test_set_track_opacity PASSED
tarunai_connect/shotcut/tests/test_core.py::TestCompositing::test_set_track_opacity_invalid_range PASSED
tarunai_connect/shotcut/tests/test_core.py::TestCompositing::test_set_track_opacity_invalid_index PASSED
tarunai_connect/shotcut/tests/test_core.py::TestCompositing::test_set_track_opacity_update_existing PASSED
tarunai_connect/shotcut/tests/test_core.py::TestCompositing::test_pip_position PASSED
tarunai_connect/shotcut/tests/test_core.py::TestCompositing::test_pip_position_defaults PASSED
tarunai_connect/shotcut/tests/test_core.py::TestCompositing::test_pip_position_invalid_track PASSED
tarunai_connect/shotcut/tests/test_core.py::TestCompositing::test_pip_position_invalid_clip PASSED
tarunai_connect/shotcut/tests/test_core.py::TestCompositing::test_pip_update_existing PASSED
tarunai_connect/shotcut/tests/test_core.py::TestCompositing::test_undo_set_blend_mode PASSED
tarunai_connect/shotcut/tests/test_core.py::TestExpandedFilters::test_filter_categories PASSED
tarunai_connect/shotcut/tests/test_core.py::TestExpandedFilters::test_chroma_key_filter_exists PASSED
tarunai_connect/shotcut/tests/test_core.py::TestExpandedFilters::test_color_grading_filters_exist PASSED
tarunai_connect/shotcut/tests/test_core.py::TestExpandedFilters::test_distortion_filters_exist PASSED
tarunai_connect/shotcut/tests/test_core.py::TestExpandedFilters::test_transform_filters_exist PASSED
tarunai_connect/shotcut/tests/test_core.py::TestExpandedFilters::test_audio_filters_exist PASSED
tarunai_connect/shotcut/tests/test_core.py::TestExpandedFilters::test_add_sharpen_filter PASSED
tarunai_connect/shotcut/tests/test_core.py::TestExpandedFilters::test_add_vignette_filter PASSED
tarunai_connect/shotcut/tests/test_core.py::TestExpandedFilters::test_add_grayscale_filter PASSED
tarunai_connect/shotcut/tests/test_core.py::TestExpandedFilters::test_add_invert_filter PASSED
tarunai_connect/shotcut/tests/test_core.py::TestExpandedFilters::test_total_filter_count PASSED
tarunai_connect/shotcut/tests/test_core.py::TestExpandedFilters::test_filter_info_has_params PASSED
```

**Summary**: 110 passed in 0.23s

## Test Breakdown

| Module | Tests | Status |
|--------|-------|--------|
| Timecode | 9 | All pass |
| MLT XML | 4 | All pass |
| Session | 7 | All pass |
| Project | 6 | All pass |
| Timeline | 17 | All pass |
| Filters | 10 | All pass |
| Media | 5 | All pass |
| Export | 5 | All pass |
| Integration | 2 | All pass |
| Transitions | 16 | All pass |
| Compositing | 16 | All pass |
| Expanded Filters | 13 | All pass |
| **Total** | **110** | **100% pass** |
